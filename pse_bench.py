"""Perspective Shift Effect benchmarking script."""

from __future__ import annotations

import argparse
import os
import time
from dataclasses import dataclass, asdict
from typing import List, Optional

import openai
import pandas as pd
import yaml
from nltk.translate.bleu_score import SmoothingFunction, sentence_bleu
from rouge_score import rouge_scorer
from rich.console import Console
from rich.table import Table


@dataclass
class Prompt:
    """Represents a single evaluation prompt."""
    prompt: str
    reference: Optional[str] = None


@dataclass
class Result:
    """Holds generation results and metrics for a single prompt."""
    prompt: str
    base_text: str
    shift_text: str
    base_latency: float
    shift_latency: float
    base_tokens: int
    shift_tokens: int
    bleu_base_shift: float
    rouge_base_shift: float
    bleu_ref_base: Optional[float] = None
    bleu_ref_shift: Optional[float] = None
    rouge_ref_base: Optional[float] = None
    rouge_ref_shift: Optional[float] = None

def load_prompts(path: str) -> List[Prompt]:
    """Load prompts from a YAML file."""
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    prompts = []
    for item in data:
        prompts.append(Prompt(prompt=item.get("prompt"), reference=item.get("reference")))
    return prompts


def call_model(model: str, prompt: str, max_tokens: int, temperature: float) -> tuple[str, float, int]:
    """Call OpenAI Chat API and return text, latency, and total tokens."""
    start = time.time()
    response = openai.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    latency = time.time() - start
    text = response.choices[0].message.content
    tokens = response.usage.total_tokens
    return text, latency, tokens

def compute_bleu(candidate: str, reference: str) -> float:
    """Compute BLEU-4 score between two texts."""
    chencherry = SmoothingFunction()
    return sentence_bleu(
        [reference.split()],
        candidate.split(),
        smoothing_function=chencherry.method1,
    )


def compute_rouge(candidate: str, reference: str) -> float:
    """Compute ROUGE-L score between two texts."""
    scorer = rouge_scorer.RougeScorer(["rougeL"], use_stemmer=True)
    scores = scorer.score(reference, candidate)
    return scores["rougeL"].fmeasure

def evaluate(
    prompts: List[Prompt],
    base_model: str,
    shift_model: str,
    max_tokens: int,
    temperature: float,
) -> List[Result]:
    """Run evaluation for each prompt."""
    results: List[Result] = []
    for p in prompts:
        base_text, base_latency, base_tokens = call_model(base_model, p.prompt, max_tokens, temperature)
        shift_text, shift_latency, shift_tokens = call_model(shift_model, p.prompt, max_tokens, temperature)

        bleu_base_shift = compute_bleu(shift_text, base_text)
        rouge_base_shift = compute_rouge(shift_text, base_text)

        bleu_ref_base = bleu_ref_shift = rouge_ref_base = rouge_ref_shift = None
        if p.reference:
            bleu_ref_base = compute_bleu(base_text, p.reference)
            bleu_ref_shift = compute_bleu(shift_text, p.reference)
            rouge_ref_base = compute_rouge(base_text, p.reference)
            rouge_ref_shift = compute_rouge(shift_text, p.reference)

        results.append(
            Result(
                prompt=p.prompt,
                base_text=base_text,
                shift_text=shift_text,
                base_latency=base_latency,
                shift_latency=shift_latency,
                base_tokens=base_tokens,
                shift_tokens=shift_tokens,
                bleu_base_shift=bleu_base_shift,
                rouge_base_shift=rouge_base_shift,
                bleu_ref_base=bleu_ref_base,
                bleu_ref_shift=bleu_ref_shift,
                rouge_ref_base=rouge_ref_base,
                rouge_ref_shift=rouge_ref_shift,
            )
        )
    return results

def summarize(results: List[Result], out_path: str) -> None:
    """Save CSV and markdown table of results."""
    df = pd.DataFrame([asdict(r) for r in results])
    df.to_csv(out_path, index=False)
    md_path = os.path.splitext(out_path)[0] + ".md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(df.to_markdown(index=False))

    console = Console()
    table = Table(title="Model Comparison")
    table.add_column("Metric")
    table.add_column("Base", justify="right")
    table.add_column("Shift", justify="right")
    table.add_column("Delta", justify="right")

    if df["bleu_ref_base"].notna().any():
        base_bleu = df["bleu_ref_base"].mean()
        shift_bleu = df["bleu_ref_shift"].mean()
        delta_bleu = shift_bleu - base_bleu
        color_bleu = "green" if delta_bleu > 0 else "red"
        table.add_row(
            "Avg BLEU vs Ref",
            f"{base_bleu:.3f}",
            f"{shift_bleu:.3f}",
            f"[bold {color_bleu}]{delta_bleu:+.3f}[/bold {color_bleu}]",
        )
    if df["rouge_ref_base"].notna().any():
        base_rouge = df["rouge_ref_base"].mean()
        shift_rouge = df["rouge_ref_shift"].mean()
        delta_rouge = shift_rouge - base_rouge
        color_rouge = "green" if delta_rouge > 0 else "red"
        table.add_row(
            "Avg ROUGE-L vs Ref",
            f"{base_rouge:.3f}",
            f"{shift_rouge:.3f}",
            f"[bold {color_rouge}]{delta_rouge:+.3f}[/bold {color_rouge}]",
        )
    console.print(table)

    if df["bleu_ref_base"].notna().any():
        if shift_bleu >= 1.5 * base_bleu:
            console.print("\n🚀 150 % lift achieved")
        else:
            console.print("\nNeeds work 😊")

def main() -> None:
    """Entry point for the benchmark script."""
    parser = argparse.ArgumentParser(description="Perspective Shift Effect benchmark")
    parser.add_argument("--max_tokens", type=int, default=128, help="Maximum tokens for generation")
    parser.add_argument("--temp", type=float, default=0.7, help="Sampling temperature")
    parser.add_argument("--out", type=str, default="results.csv", help="Output CSV path")
    args = parser.parse_args()

    base_model = os.environ.get("BASE_MODEL")
    shift_model = os.environ.get("SHIFT_MODEL")
    if not base_model or not shift_model:
        raise ValueError("BASE_MODEL and SHIFT_MODEL environment variables must be set")

    prompts = load_prompts("prompts.yml")
    results = evaluate(prompts, base_model, shift_model, args.max_tokens, args.temp)
    summarize(results, args.out)


if __name__ == "__main__":
    main()
