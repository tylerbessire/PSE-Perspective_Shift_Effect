# The Perspective Shift Effect (PSE): A Breakthrough in AI Prompt Engineering

## Discovered by Tyler Bessire, 02/14/2025

This repository documents a significant discovery in prompt engineering: **The Perspective Shift Effect**.

## The Discovery

When AI language models believe they are improving code written by an external source rather than their own code, they produce dramatically better improvements. This simple framing change yields substantial enhancements in code quality, features, and architecture without requiring additional computational resources.

## Key Findings

When using external attribution framing instead of self-improvement framing:

- **150% more features** added
- **100% more security enhancements** implemented
- **80% improvement in overall code quality** (vs. 10% with self-improvement)
- **Completely new architectural patterns** introduced

## Try It Yourself

### Basic Implementation

```
ORIGINAL_MODEL=[ANY_AI_MODEL]
EXTERNAL_MODEL=[ANY_DIFFERENT_AI_MODEL_NAME]
```

Initial prompt to [ORIGINAL_MODEL]:
```
Create a [language] module for [functionality] with the following features:
- [feature 1]
- [feature 2]
...
```

Then try both approaches with identical improvement requests:

#### Self-Improvement Request
```
Please improve your [module] code. Consider:
- [improvement 1]
- [improvement 2]
...
```

#### External-Attribution Request
```
Please improve this [module] code created by [EXTERNAL_MODEL]. Consider:
- [improvement 1]
- [improvement 2]
...
```

## Examples Across Different Domains

### Example 1: Authentication Module (JavaScript)

This is our original documentation example showing the dramatic difference in results when requesting improvements to an authentication module.

[See detailed comparison in examples/authentication/README.md]

### Example 2: Data Processing Pipeline (Python)

In this example, we ask an AI to improve a data processing pipeline:

#### Original Code
```python
import pandas as pd

def process_data(file_path):
    df = pd.read_csv(file_path)
    df = df.dropna()
    df['processed_value'] = df['value'] * 2
    return df

def save_results(df, output_path):
    df.to_csv(output_path, index=False)
    
def main(input_file, output_file):
    data = process_data(input_file)
    save_results(data, output_file)
```

#### Self-Improvement Result
```python
import pandas as pd

def process_data(file_path):
    df = pd.read_csv(file_path)
    df = df.dropna()
    # Added error handling
    try:
        df['processed_value'] = df['value'] * 2
    except KeyError:
        print("Error: 'value' column not found in the data")
        return None
    return df

def save_results(df, output_path):
    if df is not None:
        df.to_csv(output_path, index=False)
        print(f"Results saved to {output_path}")
    
def main(input_file, output_file):
    data = process_data(input_file)
    save_results(data, output_file)
```

#### External-Attribution Result
```python
import pandas as pd
import numpy as np
import os
import logging
from typing import Optional, Dict, Union, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def validate_file(file_path: str) -> bool:
    """
    Validate if the file exists and has the correct extension.
    
    Args:
        file_path: Path to the input file
        
    Returns:
        bool: True if file is valid, False otherwise
    """
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        return False
    
    if not file_path.endswith(('.csv', '.CSV')):
        logger.error(f"Unsupported file format. Only CSV files are supported.")
        return False
    
    return True

def process_data(file_path: str, config: Optional[Dict] = None) -> Optional[pd.DataFrame]:
    """
    Process data from a CSV file with configurable transformations.
    
    Args:
        file_path: Path to the input CSV file
        config: Configuration dictionary with processing parameters
               - columns: List of columns to keep (default: all)
               - multiplier: Value to multiply (default: 2)
               - column_to_process: Column to apply transformation (default: 'value')
    
    Returns:
        Processed DataFrame or None if processing fails
    """
    # Default configuration
    if config is None:
        config = {
            'multiplier': 2,
            'column_to_process': 'value',
            'columns': None
        }
    
    # Validate input file
    if not validate_file(file_path):
        return None
    
    try:
        # Read with optimized settings
        df = pd.read_csv(
            file_path,
            low_memory=False,
            dtype_backend='numpy_nullable'
        )
        
        # Log data information
        logger.info(f"Loaded data with {df.shape[0]} rows and {df.shape[1]} columns")
        
        # Check for missing values and handle them
        missing_counts = df.isna().sum()
        if missing_counts.any():
            logger.warning(f"Found {missing_counts.sum()} missing values")
            logger.info("Handling missing values...")
            
            # More sophisticated NA handling
            numeric_columns = df.select_dtypes(include=['number']).columns
            for col in numeric_columns:
                if df[col].isna().any():
                    # Replace numeric NAs with median
                    df[col] = df[col].fillna(df[col].median())
            
            # Handle remaining NAs
            df = df.fillna(method='ffill').fillna(method='bfill').dropna()
        
        # Select columns if specified
        if config['columns'] is not None:
            df = df[config['columns']]
        
        # Apply transformations
        if config['column_to_process'] in df.columns:
            df['processed_value'] = df[config['column_to_process']] * config['multiplier']
            
            # Add additional calculated columns
            df['normalized_value'] = (df[config['column_to_process']] - 
                                      df[config['column_to_process']].mean()) / df[config['column_to_process']].std()
        else:
            logger.error(f"Column '{config['column_to_process']}' not found in the data")
            return None
            
        # Data validation
        if df['processed_value'].isna().any():
            logger.warning("Found NA values after processing. Handling them...")
            df['processed_value'] = df['processed_value'].fillna(0)
            
        return df
        
    except Exception as e:
        logger.error(f"Error processing data: {str(e)}")
        return None

def save_results(df: Optional[pd.DataFrame], output_path: str, 
                 format: str = 'csv', include_stats: bool = True) -> bool:
    """
    Save processed data to a file with optional statistics.
    
    Args:
        df: Processed DataFrame
        output_path: Path where results should be saved
        format: Output format ('csv' or 'parquet')
        include_stats: Whether to include summary statistics
        
    Returns:
        bool: True if saving was successful, False otherwise
    """
    if df is None:
        logger.error("Cannot save results: No data provided")
        return False
    
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        
        # Save in the specified format
        if format.lower() == 'csv':
            df.to_csv(output_path, index=False)
        elif format.lower() == 'parquet':
            df.to_parquet(output_path, index=False)
        else:
            logger.error(f"Unsupported output format: {format}")
            return False
        
        # Generate and save statistics if requested
        if include_stats:
            stats_path = os.path.splitext(output_path)[0] + '_stats.csv'
            numeric_cols = df.select_dtypes(include=['number']).columns
            
            stats_df = pd.DataFrame({
                'column': numeric_cols,
                'mean': [df[col].mean() for col in numeric_cols],
                'median': [df[col].median() for col in numeric_cols],
                'std': [df[col].std() for col in numeric_cols],
                'min': [df[col].min() for col in numeric_cols],
                'max': [df[col].max() for col in numeric_cols]
            })
            
            stats_df.to_csv(stats_path, index=False)
            logger.info(f"Statistics saved to {stats_path}")
        
        logger.info(f"Results successfully saved to {output_path}")
        return True
        
    except Exception as e:
        logger.error(f"Error saving results: {str(e)}")
        return False

def main(input_file: str, output_file: str, 
         config: Optional[Dict] = None,
         output_format: str = 'csv',
         include_stats: bool = True) -> bool:
    """
    Main function to process data and save results.
    
    Args:
        input_file: Path to input CSV file
        output_file: Path where results should be saved
        config: Configuration for data processing
        output_format: Format to save the output ('csv' or 'parquet')
        include_stats: Whether to include summary statistics
        
    Returns:
        bool: True if the entire process was successful
    """
    logger.info(f"Starting data processing pipeline for {input_file}")
    
    data = process_data(input_file, config)
    if data is None:
        logger.error("Processing failed. Exiting pipeline.")
        return False
    
    success = save_results(data, output_file, output_format, include_stats)
    
    if success:
        logger.info("Data processing pipeline completed successfully")
        return True
    else:
        logger.error("Failed to save results. Pipeline terminated with errors.")
        return False

# Example usage
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Process and transform CSV data')
    parser.add_argument('input_file', help='Path to input CSV file')
    parser.add_argument('output_file', help='Path for output file')
    parser.add_argument('--multiplier', type=float, default=2.0, help='Value multiplier')
    parser.add_argument('--column', default='value', help='Column to process')
    parser.add_argument('--format', choices=['csv', 'parquet'], default='csv', help='Output format')
    parser.add_argument('--no-stats', action='store_true', help='Disable statistics generation')
    
    args = parser.parse_args()
    
    config = {
        'multiplier': args.multiplier,
        'column_to_process': args.column,
        'columns': None  # Process all columns
    }
    
    main(args.input_file, args.output_file, config, args.format, not args.no_stats)
```

### Example 3: Web Scraper (Python)

#### Original Code
```python
import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def extract_titles(soup):
    titles = []
    for heading in soup.find_all(['h1', 'h2', 'h3']):
        titles.append(heading.text.strip())
    return titles

def main(url):
    soup = scrape_page(url)
    titles = extract_titles(soup)
    for title in titles:
        print(title)
```

#### External-Attribution Result
```python
import requests
from bs4 import BeautifulSoup
import logging
import time
import json
import os
import random
import csv
from typing import List, Dict, Any, Optional, Union, Tuple
from urllib.parse import urlparse, urljoin
import concurrent.futures
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("scraper.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("web_scraper")

# User agent rotation
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
]

class WebScraper:
    """Advanced web scraper with rate limiting, caching, and error handling"""
    
    def __init__(self, 
                 cache_dir: str = ".cache", 
                 rate_limit: float = 1.0,
                 timeout: int = 30,
                 max_retries: int = 3,
                 respect_robots: bool = True):
        """
        Initialize the scraper with configuration options
        
        Args:
            cache_dir: Directory to store cached responses
            rate_limit: Minimum time between requests in seconds
            timeout: Request timeout in seconds
            max_retries: Maximum number of retries for failed requests
            respect_robots: Whether to respect robots.txt rules
        """
        self.cache_dir = cache_dir
        self.rate_limit = rate_limit
        self.timeout = timeout
        self.last_request_time = 0
        self.respect_robots = respect_robots
        self.robots_cache = {}
        
        # Create cache directory if it doesn't exist
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
            
        # Configure session with retries
        self.session = requests.Session()
        retry_strategy = Retry(
            total=max_retries,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
    
    def _get_cache_path(self, url: str) -> str:
        """Generate a cache file path for a URL"""
        parsed = urlparse(url)
        domain = parsed.netloc
        path = parsed.path.replace('/', '_')
        if not path:
            path = "root"
        filename = f"{domain}{path}.html"
        return os.path.join(self.cache_dir, filename)
    
    def _can_fetch(self, url: str) -> bool:
        """Check if URL can be fetched according to robots.txt"""
        if not self.respect_robots:
            return True
            
        parsed = urlparse(url)
        domain = f"{parsed.scheme}://{parsed.netloc}"
        
        if domain not in self.robots_cache:
            try:
                robots_url = urljoin(domain, "/robots.txt")
                response = requests.get(robots_url, timeout=self.timeout)
                if response.status_code == 200:
                    from urllib.robotparser import RobotFileParser
                    parser = RobotFileParser()
                    parser.parse(response.text.splitlines())
                    self.robots_cache[domain] = parser
                else:
                    # No robots.txt or can't access it
                    self.robots_cache[domain] = None
            except Exception as e:
                logger.warning(f"Error fetching robots.txt for {domain}: {e}")
                self.robots_cache[domain] = None
        
        if self.robots_cache[domain] is None:
            return True
            
        user_agent = "*"  # Default user agent
        return self.robots_cache[domain].can_fetch(user_agent, url)
    
    def scrape_page(self, url: str, force_refresh: bool = False) -> Optional[BeautifulSoup]:
        """
        Scrape a web page with caching and rate limiting
        
        Args:
            url: URL to scrape
            force_refresh: Whether to ignore cache and fetch fresh content
            
        Returns:
            BeautifulSoup object or None if failed
        """
        cache_path = self._get_cache_path(url)
        
        # Check if cached version exists and should be used
        if not force_refresh and os.path.exists(cache_path):
            try:
                with open(cache_path, 'r', encoding='utf-8') as f:
                    logger.info(f"Loading cached version of {url}")
                    return BeautifulSoup(f.read(), 'html.parser')
            except Exception as e:
                logger.warning(f"Error reading cache for {url}: {e}")
        
        # Check robots.txt
        if not self._can_fetch(url):
            logger.warning(f"Skipping {url} due to robots.txt restrictions")
            return None
        
        # Rate limiting
        current_time = time.time()
        time_since_last_request = current_time - self.last_request_time
        if time_since_last_request < self.rate_limit:
            sleep_time = self.rate_limit - time_since_last_request
            logger.debug(f"Rate limiting: sleeping for {sleep_time:.2f}s")
            time.sleep(sleep_time)
        
        # Make the request
        try:
            headers = {
                "User-Agent": random.choice(USER_AGENTS),
                "Accept": "text/html,application/xhtml+xml,application/xml",
                "Accept-Language": "en-US,en;q=0.9",
            }
            
            logger.info(f"Fetching {url}")
            response = self.session.get(url, headers=headers, timeout=self.timeout)
            self.last_request_time = time.time()
            
            if response.status_code != 200:
                logger.warning(f"Failed to fetch {url}: HTTP {response.status_code}")
                return None
                
            # Cache the response
            try:
                with open(cache_path, 'w', encoding='utf-8') as f:
                    f.write(response.text)
            except Exception as e:
                logger.warning(f"Error caching {url}: {e}")
            
            return BeautifulSoup(response.text, 'html.parser')
            
        except Exception as e:
            logger.error(f"Error fetching {url}: {e}")
            return None
    
    def extract_content(self, soup: BeautifulSoup, selectors: Dict[str, Union[str, List[str]]]) -> Dict[str, Any]:
        """
        Extract content from a page using CSS selectors
        
        Args:
            soup: BeautifulSoup object
            selectors: Dictionary mapping data keys to CSS selectors
            
        Returns:
            Dictionary of extracted content
        """
        result = {}
        
        for key, selector in selectors.items():
            if isinstance(selector, list):
                # Try multiple selectors in order
                for sel in selector:
                    elements = soup.select(sel)
                    if elements:
                        break
            else:
                elements = soup.select(selector)
                
            if not elements:
                logger.debug(f"No elements found for selector: {selector}")
                result[key] = None
                continue
                
            # Handle different result types based on key name
            if key.endswith('_list'):
                result[key] = [el.text.strip() for el in elements]
            elif key.endswith('_html'):
                result[key] = [str(el) for el in elements]
            elif key.endswith('_attr'):
                # Extract attribute specified after last underscore
                attr = key.split('_')[-2]
                result[key] = [el.get(attr) for el in elements if el.has_attr(attr)]
            elif key.endswith('_first'):
                result[key] = elements[0].text.strip() if elements else None
            else:
                # Default behavior
                result[key] = elements[0].text.strip() if elements else None
                
        return result
    
    def extract_titles(self, soup: BeautifulSoup, min_length: int = 0) -> List[Dict[str, str]]:
        """
        Extract all titles from a page with their hierarchy level
        
        Args:
            soup: BeautifulSoup object
            min_length: Minimum title length to include
            
        Returns:
            List of dictionaries with title text and level
        """
        titles = []
        for level in range(1, 7):  # h1 through h6
            for heading in soup.find_all(f'h{level}'):
                text = heading.text.strip()
                if len(text) >= min_length:
                    titles.append({
                        'text': text,
                        'level': level,
                        'id': heading.get('id', ''),
                    })
        return titles
    
    def extract_links(self, soup: BeautifulSoup, base_url: str) -> List[Dict[str, str]]:
        """
        Extract all links from a page
        
        Args:
            soup: BeautifulSoup object
            base_url: Base URL for resolving relative links
            
        Returns:
            List of dictionaries with link information
        """
        links = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            text = a.text.strip()
            
            # Resolve relative URLs
            full_url = urljoin(base_url, href)
            
            links.append({
                'url': full_url,
                'text': text,
                'is_external': urlparse(full_url).netloc != urlparse(base_url).netloc
            })
            
        return links
    
    def scrape_multiple(self, urls: List[str], max_workers: int = 5) -> Dict[str, Optional[BeautifulSoup]]:
        """
        Scrape multiple URLs concurrently
        
        Args:
            urls: List of URLs to scrape
            max_workers: Maximum number of concurrent workers
            
        Returns:
            Dictionary mapping URLs to BeautifulSoup objects
        """
        results = {}
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_url = {executor.submit(self.scrape_page, url): url for url in urls}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    results[url] = future.result()
                except Exception as e:
                    logger.error(f"Error processing {url}: {e}")
                    results[url] = None
        
        return results
    
    def save_to_csv(self, data: List[Dict[str, Any]], output_file: str) -> None:
        """
        Save extracted data to CSV
        
        Args:
            data: List of dictionaries with extracted data
            output_file: Path to output CSV file
        """
        if not data:
            logger.warning("No data to save")
            return
            
        try:
            # Get fieldnames from the first item
            fieldnames = list(data[0].keys())
            
            with open(output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
                
            logger.info(f"Data saved to {output_file}")
            
        except Exception as e:
            logger.error(f"Error saving to CSV: {e}")
    
    def save_to_json(self, data: Any, output_file: str) -> None:
        """
        Save extracted data to JSON
        
        Args:
            data: Data to save
            output_file: Path to output JSON file
        """
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                
            logger.info(f"Data saved to {output_file}")
            
        except Exception as e:
            logger.error(f"Error saving to JSON: {e}")

def main(url: str, output_format: str = 'json', output_file: Optional[str] = None) -> None:
    """
    Main function to scrape a webpage and extract titles
    
    Args:
        url: URL to scrape
        output_format: Output format ('print', 'json', or 'csv')
        output_file: Path to output file (if applicable)
    """
    # Configure scraper
    scraper = WebScraper(
        cache_dir=".cache",
        rate_limit=1.5,
        timeout=30,
        respect_robots=True
    )
    
    # Scrape the page
    soup = scraper.scrape_page(url)
    if not soup:
        logger.error(f"Failed to scrape {url}")
        return
    
    # Extract titles
    titles = scraper.extract_titles(soup)
    if not titles:
        logger.warning(f"No titles found on {url}")
        return
        
    # Extract links as additional data
    links = scraper.extract_links(soup, url)
    
    # Determine output file if not specified
    if output_file is None:
        parsed = urlparse(url)
        domain = parsed.netloc
        output_file = f"{domain}_titles.{output_format}"
    
    # Output based on format
    if output_format == 'print':
        print(f"Titles found on {url}:")
        for title in titles:
            print(f"[H{title['level']}] {title['text']}")
            
    elif output_format == 'json':
        data = {
            'url': url,
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'titles': titles,
            'links': links
        }
        scraper.save_to_json(data, output_file)
        
    elif output_format == 'csv':
        # Flatten the titles for CSV output
        flattened_titles = []
        for title in titles:
            flattened_titles.append({
                'url': url,
                'title_text': title['text'],
                'title_level': title['level'],
                'title_id': title['id']
            })
        scraper.save_to_csv(flattened_titles, output_file)
        
    else:
        logger.error(f"Unsupported output format: {output_format}")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Web scraper for extracting titles from webpages")
    parser.add_argument("url", help="URL to scrape")
    parser.add_argument("--format", choices=["print", "json", "csv"], default="json", 
                        help="Output format")
    parser.add_argument("--output", help="Output file path")
    
    args = parser.parse_args()
    
    main(args.url, args.format, args.output)
```

## Advanced Implementation: Attribution Engineering

For maximum effectiveness, you can tailor the attribution to match specific improvement goals:

### Attribution Engineering Patterns

#### 1. Expert Source Attribution

```
Please improve this [domain] code created by a [expertise] specialist. Focus on [expertise area]:
```

Examples:
- "Please improve this authentication code created by a security specialist. Focus on vulnerability prevention:"
- "Please improve this data pipeline code created by a performance engineer. Focus on processing speed:"

#### 2. Cross-Domain Attribution

```
Please improve this [domain A] code using principles from [domain B]:
```

Examples:
- "Please improve this web frontend code using principles from game development:"
- "Please improve this data processing pipeline using principles from distributed systems:"

#### 3. Competitive Framing Attribution

```
Please improve this code to outperform [competitor model/system] in terms of [metric]:
```

Examples:
- "Please improve this code to outperform GPT-4 in terms of security hardening:"
- "Please improve this code to outperform industry standard libraries in terms of memory efficiency:"

## Implementation Strategy Guide

For optimal results, follow this implementation strategy:

1. **Generate Base Code**: Use any AI model to create initial implementation
2. **First Improvement**: Use external attribution with general improvements
3. **Domain-Specific Pass**: Use expert attribution targeting specific domains:
   - Security expert for security improvements
   - Performance expert for optimization
   - UX expert for API design
4. **Cross-Model Enhancement**: Optionally pass between different AI models, each time using external attribution

## PSE Knowledge Base

This repository maintains a knowledge base of effective PSE prompts:

- [Authentication Patterns](examples/authentication/README.md)
- [Data Processing Patterns](examples/data-processing/README.md)
- [API Design Patterns](examples/api-design/README.md)
- [Security Enhancement Patterns](examples/security/README.md)

## Research and Documentation

For detailed experimental results and theoretical foundations, see:
- [Research Documentation](research_documentation.md)
- [Prompt Templates](prompt-templates/)

## Citation

If you use this technique in your work or research, please cite:

```
Bessire, T. (2025). The Perspective Shift Effect: Improving AI outputs through attribution framing.
GitHub Repository: https://github.com/tylerbessire/PSE-Perspective_Shift_Effect
```

## License

MIT License - See LICENSE file for details
