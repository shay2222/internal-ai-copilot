
# Evaluation Results

## Summary
- Category accuracy: **3/3**
- Urgency accuracy: **3/3**
- Validation passed on test examples: **Yes**

## Notes
The current rule-based extractor correctly classified all three test examples for both category and urgency. 

Example successful extraction:
- Input: "Hi, I was charged twice for my subscription this month. Can someone help me get a refund?"
- Output: category = billing, urgency = high

This gives a clean baseline. The next improvement would be replacing the rules with a proper LLM structured-extraction call while keeping the same validation and evaluation harness.
