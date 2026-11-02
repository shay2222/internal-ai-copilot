# internal-ai-copilot
A free, end-to-end demonstration of an AI tool that turns messy support and operations tickets into clean structured data.

**What it does:**  
Takes raw ticket text and returns:
- Category
- Urgency
- Summary
- Recommended next action

This project shows the full loop that production AI teams care about: clear problem definition, structured extraction, validation, evaluation, and simple tooling.

---

## Why this exists

Support and operations teams often receive unstructured tickets. Manual triage is slow and inconsistent. This demo shows a practical way to turn free-text into reliable structured output that an internal team can actually use.

---

## Current Demo Results

- Category accuracy: **3/3**
- Urgency accuracy: **3/3**
- Validation: **Passed**

  
## Project Structure
internal-ai-copilot/
├── README.md
├── PROJECT_GOAL.md
├── requirements.txt
├── docs/
│   └── architecture.md
├── data/
│   └── sample_tickets.csv
├── evaluation/
│   ├── test_questions.csv
│   └── results.md
└── src/


## How to Run the Demo
- Open the Colab notebook (or copy the functions into your own notebook).
- Run the extraction and validation cells.
- Test with any ticket text using the run_copilot() function.
The current version uses a simple, fully reproducible rule-based extractor so everything runs for free. The design makes it easy to later swap in a real LLM structured-extraction layer while keeping the same validation and evaluation harness.

## Architecture
See the full write-up here:

docs/architecture.md 

Key points:
- Structured output with schema validation
- Clear separation between extraction, validation, and interface
- Evaluation against labeled examples
- Written with production concerns in mind (logging, failure modes, future LLM swap)

## Evaluation
Detailed results are in evaluation/results.md.
The current baseline correctly classified all test examples for both category and urgency


## Limitations
- Uses a simple rule-based extractor for full free reproducibility
- Small evaluation set (intentionally narrow for a clean first version)
- Designed so a real LLM structured-extraction model can replace the rules later without changing the rest of the system

Example output:
```json
{
  "category": "billing",
  "urgency": "high",
  "summary": "Hi, I was charged twice for my subscription this month...",
  "recommended_next_action": "Review billing records and respond within 4 hours"
}



