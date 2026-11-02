# Architecture – Internal AI Copilot

## 1. Problem
Support and operations teams receive unstructured tickets. Manual triage is slow and inconsistent.

## 2. Goal
Turn free-text tickets into structured data (category, urgency, summary, next action) reliably.

## 3. High-Level Design
- Input: raw ticket text
- Processing: rule-based + LLM-ready extraction layer
- Validation: schema checks
- Output: structured JSON + recommended action
- Evaluation: accuracy against labeled examples

## 4. Components
- Extraction function
- Validation layer
- Simple evaluation harness
- Interface for internal users

## 5. Production Considerations
- Schema validation and retries
- Logging of every prediction
- Clear failure modes
- Cost and latency tracking
- How this would be deployed behind an API

## 6. Limitations of this demo
- Currently uses a simple rule-based extractor for full reproducibility on free tools
- Designed so a real LLM structured-extraction layer can replace the rules later
