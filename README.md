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

Example output:
```json
{
  "category": "billing",
  "urgency": "high",
  "summary": "Hi, I was charged twice for my subscription this month...",
  "recommended_next_action": "Review billing records and respond within 4 hours"
}


- Designed so a real LLM structured-extraction model can replace the rules later without changing the rest of the system
