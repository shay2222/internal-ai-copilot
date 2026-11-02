# Architecture – Internal AI Copilot

## 1. Problem
Support and operations teams receive unstructured tickets. Manual triage is slow and inconsistent.

## 2. Goal
Turn free-text tickets into structured data (category, urgency, summary, next action) reliably.

## 3. High-Level Design
- Input: raw ticket text
- Processing: rule-based extraction layer (designed so an LLM structured-extraction layer can replace it later)
- Validation: schema checks for category, urgency, summary, and recommended action
- Output: structured JSON + recommended next action
- Evaluation: accuracy against labeled examples

## 4. Components
- Extraction function (`simple_extract`)
- Validation layer (`validate_output`)
- Simple evaluation harness
- Function-based interface (`run_copilot`)

## 5. Current Results (from demo run)
- Validation: Passed (`Valid: True`)
- Category accuracy: 3/3
- Urgency accuracy: 3/3

Example output:
```json
{
  "category": "billing",
  "urgency": "high",
  "summary": "Hi, I was charged twice for my subscription this month...",
  "recommended_next_action": "Review billing records and respond within 4 hours"
}
