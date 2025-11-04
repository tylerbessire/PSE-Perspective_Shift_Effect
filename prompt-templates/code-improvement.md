# Advanced Prompt Engineering Templates

This document provides comprehensive, production-grade prompt templates demonstrating the **Perspective Shift Effect (PSE)** and top-tier prompt engineering practices.

---

## Table of Contents
1. [Code Improvement Templates](#code-improvement-templates)
2. [Technical Analysis Templates](#technical-analysis-templates)
3. [System Design Templates](#system-design-templates)
4. [Documentation Templates](#documentation-templates)
5. [Best Practices & Principles](#best-practices--principles)

---

## Code Improvement Templates

### Template 1: Basic PSE Application

#### Self-Attribution Version (Baseline)
```
Please improve your implementation of [component/feature].

Requirements:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

Deliverables:
- Refactored code
- Explanation of improvements
```

#### External Attribution Version (PSE Enhanced)
```
Please improve this [component/feature] implementation created by [expert/team/source].

Requirements:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

Deliverables:
- Refactored code with detailed commentary
- Explanation of improvements with justifications
- Performance/security impact analysis
```

**Expected Lift**: 15-30% improvement in code quality metrics

---

### Template 2: Advanced Attribution Engineering

#### Multi-Dimensional Attribution
```
Please review and enhance this [code/system] originally designed by [source] and
refined by [expertise type] engineers.

Context:
- Original purpose: [description]
- Current limitations: [issues]
- Performance requirements: [metrics]
- Security constraints: [requirements]

Analysis Required:
1. Architecture assessment
2. Security vulnerability analysis
3. Performance bottleneck identification
4. Scalability evaluation

Deliverables:
1. Comprehensive analysis report
2. Prioritized improvement recommendations
3. Refactored implementation with explanations
4. Test cases for critical paths
5. Migration strategy (if applicable)

Focus particularly on [specific area] from a [expert perspective] viewpoint.
```

**Expert Perspectives to Consider**:
- Security researcher: Focus on threat modeling, attack vectors
- Performance engineer: Focus on optimization, profiling, benchmarking
- Site reliability engineer: Focus on observability, resilience, fault tolerance
- Principal architect: Focus on maintainability, extensibility, patterns
- Junior developer (for reviewing): Focus on readability, documentation, clarity

---

### Template 3: Structured Code Review

#### Expert-Attributed Code Review
```
You are conducting a code review as a [senior engineer/tech lead/security expert]
for this [language/framework] implementation originally written by [source].

Code to Review:
```[language]
[CODE_BLOCK]
```

Review Criteria:
1. **Correctness**: Logic errors, edge cases, algorithmic issues
2. **Security**: Vulnerabilities, input validation, authorization
3. **Performance**: Time/space complexity, bottlenecks, optimizations
4. **Maintainability**: Code clarity, naming, structure, comments
5. **Best Practices**: Language idioms, framework patterns, style guides
6. **Testing**: Test coverage, testability, error scenarios

Format:
For each issue found:
- **Severity**: Critical | High | Medium | Low
- **Category**: [One of the criteria above]
- **Issue**: [Clear description]
- **Location**: [Line numbers or function names]
- **Impact**: [What could go wrong]
- **Recommendation**: [Specific fix with code example]

Summary:
- Total issues by severity
- Top 3 priorities
- Estimated refactoring effort
- Overall code quality score (1-10)
```

---

## Technical Analysis Templates

### Template 4: Systematic Debugging

#### Structured Problem Analysis
```
You are a [senior debugging expert/systems engineer] investigating a production issue
in a [system type] originally built by [team/company].

**Problem Statement**:
[Detailed description of the issue]

**Observable Symptoms**:
- [Symptom 1 with metrics]
- [Symptom 2 with metrics]
- [Symptom 3 with metrics]

**System Context**:
- Architecture: [description]
- Technology stack: [list]
- Scale: [metrics]
- Recent changes: [list]

**Analysis Framework**:
1. **Hypothesis Generation**
   - List 5-7 potential root causes
   - Rank by likelihood (High/Medium/Low)
   - Provide reasoning for each

2. **Diagnostic Strategy**
   - For each hypothesis, specify:
     * What to measure/test
     * How to isolate variables
     * Expected results if hypothesis is correct
     * Expected results if hypothesis is incorrect

3. **Root Cause Analysis**
   - Evidence-based conclusion
   - Distinguish correlation from causation
   - Identify contributing factors vs. root cause

4. **Solution Design**
   - Immediate mitigation (if urgent)
   - Short-term fix
   - Long-term solution
   - Prevention strategy

5. **Validation Plan**
   - How to verify the fix works
   - Metrics to monitor
   - Rollback criteria

**Deliverables**:
- Ranked hypothesis list
- Diagnostic test plan
- Root cause determination
- Tiered solution recommendations
- Monitoring/alerting improvements
```

---

### Template 5: Performance Optimization

#### Attributed Performance Analysis
```
You are a [performance engineering specialist] analyzing a [system/application]
created by [source] for optimization opportunities.

**Current Performance Profile**:
- Metric 1: [current value] (target: [target value])
- Metric 2: [current value] (target: [target value])
- Metric 3: [current value] (target: [target value])

**System Specifications**:
- Language/Framework: [details]
- Infrastructure: [details]
- Traffic patterns: [details]
- Data volume: [details]

**Analysis Required**:

1. **Profiling**
   - Identify top CPU/memory/I/O hotspots
   - Analyze algorithmic complexity
   - Measure allocation patterns
   - Identify lock contention (if applicable)

2. **Optimization Opportunities**
   For each opportunity, provide:
   - Current implementation
   - Performance impact (quantified)
   - Proposed optimization
   - Expected improvement (estimate)
   - Implementation complexity (Low/Medium/High)
   - Risk assessment

3. **Prioritization**
   - Order by ROI (impact/effort ratio)
   - Consider business priorities
   - Account for technical debt

4. **Implementation Plan**
   - Quick wins (< 1 day)
   - Medium optimizations (1-5 days)
   - Major refactoring (> 5 days)
   - For each: steps, validation, rollback plan

**Deliverables**:
- Performance bottleneck analysis
- Prioritized optimization backlog
- Detailed implementation plan for top 3 items
- Benchmarking strategy
- Long-term performance architecture recommendations
```

---

## System Design Templates

### Template 6: Scalable Architecture Design

#### Expert-Attributed System Design
```
You are a [principal architect/staff engineer] designing a [system type] for [use case].

**Requirements**:

*Functional*:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]

*Non-Functional*:
- Scale: [metrics - QPS, DAU, data volume]
- Latency: [requirements - p50, p95, p99]
- Availability: [target - 99.9%, 99.99%]
- Consistency: [requirements - strong, eventual]
- Cost: [constraints]

**Design Deliverables**:

1. **High-Level Architecture**
   - System diagram (describe components and data flow)
   - Key components with responsibilities
   - Technology stack with justifications
   - Data flow for primary use cases

2. **Detailed Component Design**
   For each major component:
   - Interface/API specification
   - Internal architecture
   - Technology choice rationale
   - Scaling strategy
   - Failure modes and mitigations

3. **Data Model**
   - Schema design (SQL/NoSQL)
   - Partitioning/sharding strategy
   - Indexing strategy
   - Data retention policy
   - Migration plan

4. **Trade-off Analysis**
   - CAP theorem considerations
   - Consistency vs. availability choices
   - Cost vs. performance trade-offs
   - Complexity vs. flexibility decisions
   - Explicit assumptions made

5. **Operational Considerations**
   - Monitoring and alerting strategy
   - Deployment approach
   - Disaster recovery plan
   - Security architecture
   - Testing strategy

6. **Capacity Planning**
   - Resource estimation (CPU, memory, storage, network)
   - Growth projections (1 year, 3 years)
   - Cost modeling
   - Scaling triggers

7. **Alternative Approaches**
   - Other architectures considered
   - Why they were rejected
   - Circumstances where they might be better

**Format**:
Use clear sections, diagrams (described in text), and explain all decisions.
```

---

### Template 7: API Design

#### Expert-Attributed API Design
```
You are a [senior API architect] designing a [REST/GraphQL/gRPC] API for [use case],
building upon patterns from [company/framework/standard].

**API Scope**: [Description]

**Design Principles**:
- RESTful/GraphQL/gRPC best practices
- Backward compatibility
- Developer experience
- Performance
- Security

**Required Sections**:

1. **API Overview**
   - Purpose and scope
   - Target audience (internal/external developers)
   - Key use cases
   - Rate limits and quotas

2. **Endpoint Design** (for each endpoint)
   - HTTP method and path (REST) or operation (GraphQL/gRPC)
   - Purpose and use case
   - Request parameters (path, query, headers, body)
   - Response format (success and error cases)
   - Status codes with meanings
   - Examples (request + response)

3. **Data Models**
   - Schema definitions (JSON Schema, Protobuf, GraphQL types)
   - Validation rules
   - Optional vs. required fields
   - Default values

4. **Authentication & Authorization**
   - Auth mechanism (OAuth, API keys, JWT)
   - Permission model
   - Token lifecycle
   - Security best practices

5. **Error Handling**
   - Error response format
   - Error codes and meanings
   - Retry strategies
   - Rate limit headers

6. **Pagination**
   - Pagination approach (offset, cursor, page-based)
   - Default and max page sizes
   - Response metadata

7. **Versioning Strategy**
   - Versioning approach (URL, header, content negotiation)
   - Deprecation policy
   - Migration guide template

8. **Performance**
   - Caching strategy
   - Compression
   - Batch operations
   - Async operations (if applicable)

9. **Documentation**
   - OpenAPI/GraphQL schema
   - Interactive documentation
   - Code examples (multiple languages)
   - Quickstart guide

**Quality Criteria**:
- Consistency across endpoints
- Intuitive naming
- Proper HTTP semantics
- Clear error messages
- Developer-friendly
```

---

## Documentation Templates

### Template 8: Technical Documentation

#### Expert-Attributed Technical Writing
```
You are a [senior technical writer/developer advocate] creating documentation
for [system/API/library] used by [target audience].

**Documentation Type**: [Tutorial/How-to/Reference/Explanation]

**Audience Profile**:
- Experience level: [Beginner/Intermediate/Advanced]
- Prior knowledge: [List prerequisites]
- Goals: [What they want to achieve]

**Structure** (adapt based on doc type):

1. **Introduction**
   - What is this?
   - Why would you use it?
   - When should you use it (vs. alternatives)?
   - Quick example showing value

2. **Getting Started** (for tutorials)
   - Prerequisites
   - Installation/setup
   - "Hello World" example
   - Expected output
   - Common issues

3. **Core Concepts** (for explanations)
   - Key terminology (glossary)
   - Mental models
   - Diagrams
   - Analogies for complex concepts

4. **Detailed Guide** (for how-tos)
   - Step-by-step instructions
   - Code examples
   - Expected results
   - Troubleshooting
   - Alternative approaches

5. **Reference** (for API docs)
   - Comprehensive parameter listings
   - Return values
   - Error conditions
   - Examples for each function/endpoint

6. **Best Practices**
   - Recommended patterns
   - Anti-patterns to avoid
   - Performance tips
   - Security considerations

7. **Advanced Topics**
   - Complex use cases
   - Optimization techniques
   - Integration patterns
   - Customization options

8. **Troubleshooting**
   - Common errors
   - Debugging strategies
   - FAQ
   - How to get help

**Writing Guidelines**:
- Use active voice
- Short sentences and paragraphs
- Code examples are tested and runnable
- Include context before details
- Progressive disclosure (simple → complex)
- Scannable structure (headers, bullets, code blocks)
- Examples use realistic scenarios
- Explain the "why," not just the "how"
```

---

## Best Practices & Principles

### Core Prompt Engineering Principles

1. **Specificity Over Vagueness**
   - ❌ "Make this code better"
   - ✅ "Optimize this code for time complexity, reducing from O(n²) to O(n log n) while maintaining readability"

2. **Context Provision**
   - Always provide: purpose, constraints, audience, success criteria
   - Include: current state, desired state, why it matters

3. **Structured Output Requests**
   - Use numbered lists, sections, tables
   - Specify format explicitly
   - Request examples, not just theory

4. **Attribution Engineering (PSE)**
   - Attribute code/designs to credible sources
   - Specify expertise type (security, performance, UX)
   - Use actual company/framework patterns

5. **Role-Based Prompting**
   - "You are a [specific expert role]..."
   - Provides context on perspective and priorities
   - Influences tone, depth, and focus

6. **Constraint Specification**
   - Performance requirements
   - Security requirements
   - Compatibility requirements
   - Resource constraints

7. **Multi-Step Reasoning**
   - Request analysis before solution
   - Ask for trade-off discussions
   - Require justifications for choices

8. **Quality Criteria Definition**
   - What does "good" look like?
   - Metrics for success
   - How to validate the output

9. **Example Provision** (Few-Shot Learning)
   - Show desired format with examples
   - Demonstrate quality bar
   - Illustrate edge cases

10. **Iterative Refinement**
    - Start broad, narrow down
    - Request alternatives
    - Ask for critique of own suggestions

---

### PSE Application Strategies

#### Strategy 1: Source Attribution
Attribute code/systems to credible entities:
- Companies: "Google's version of...", "Netflix's approach to..."
- Frameworks: "Following Django's patterns...", "Based on React's architecture..."
- Standards: "Compliant with RFC 7519...", "Following OWASP guidelines..."

#### Strategy 2: Expertise Attribution
Specify the type of expert perspective:
- Domain: "security researcher", "ML engineer", "frontend specialist"
- Level: "senior", "principal", "staff engineer"
- Company tier: "FAANG engineer", "startup CTO"

#### Strategy 3: Comparative Attribution
Compare multiple approaches:
- "Compare implementation A (from Source X) with approach B (from Source Y)"
- "Evaluate this design against patterns from [Framework]"

#### Strategy 4: Chain Attribution
Layer multiple attributions:
- "This was originally built by [Team A], refactored by [Expert B], now you as [Expert C] are reviewing it"

---

### Measuring Prompt Effectiveness

**Key Metrics**:
1. **Relevance**: Does output address the request?
2. **Accuracy**: Is information correct?
3. **Completeness**: Are all aspects covered?
4. **Depth**: Sufficient detail vs. superficiality?
5. **Structure**: Well-organized and scannable?
6. **Actionability**: Can you directly use this?
7. **Novelty**: New insights vs. generic advice?

**A/B Testing Framework**:
- Baseline prompt (control)
- Enhanced prompt with PSE (treatment)
- Compare outputs using metrics above
- Measure using BLEU, ROUGE, or human evaluation

---

### Common Anti-Patterns

❌ **Don't:**
- Use vague language: "improve", "optimize", "make better"
- Omit constraints and requirements
- Forget to specify output format
- Ask multiple unrelated questions in one prompt
- Assume context that wasn't provided
- Accept first output without iteration

✅ **Do:**
- Be specific about what and why
- Provide comprehensive context
- Structure requests clearly
- One primary goal per prompt (or clearly separated)
- Explicitly state all requirements
- Review and refine prompts based on results

---

### Template Usage Guide

**Selecting the Right Template**:
1. Identify your goal (code review, design, documentation)
2. Choose appropriate template from this document
3. Fill in all bracketed placeholders
4. Add context specific to your use case
5. Review completeness before submission

**Customization Tips**:
- Adjust expertise level to match your needs
- Add domain-specific requirements
- Modify deliverables section for your context
- Include actual examples where possible
- Specify output format preferences

**Evaluation**:
- Does the prompt clearly communicate what you need?
- Would someone unfamiliar with the context understand it?
- Are success criteria explicit?
- Is the expected output format clear?

---

### Advanced Techniques

#### Technique 1: Constraint-Based Generation
```
Generate [output] with these constraints:
- MUST: [Hard requirements]
- SHOULD: [Soft requirements]
- MUST NOT: [Forbidden elements]
- PREFER: [Nice-to-haves]
```

#### Technique 2: Socratic Prompting
```
Before providing a solution:
1. What are the key challenges in this problem?
2. What trade-offs need to be considered?
3. What are 3 alternative approaches?
4. What are the pros/cons of each?
5. Now, provide your recommended solution with justification.
```

#### Technique 3: Red Team Prompting
```
First, provide your solution to [problem].

Then, as a critical reviewer:
- Identify weaknesses in your solution
- Propose adversarial test cases
- Suggest improvements based on critique
- Provide revised solution
```

#### Technique 4: Incremental Complexity
```
Level 1: Provide a basic solution that works
Level 2: Enhance it with error handling
Level 3: Add performance optimizations
Level 4: Make it production-ready with monitoring, logging, tests
Level 5: Design for scale and reliability
```

---

## Conclusion

These templates represent state-of-the-art prompt engineering practices, incorporating:
- **Perspective Shift Effect** for improved output quality
- **Structured reasoning** for comprehensive responses
- **Role-based prompting** for expert-level insights
- **Clear expectations** for actionable results

**Next Steps**:
1. Select appropriate template for your use case
2. Customize with specific requirements
3. Test and iterate based on results
4. Measure effectiveness using provided metrics
5. Refine prompts based on outcomes

**Remember**: The best prompts are specific, contextual, structured, and iterative.

---

*For more information on the Perspective Shift Effect, see: [research_documentation.md](../research_documentation.md)*
