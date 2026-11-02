CATEGORIES = ["billing", "bug", "feature_request", "other"]
URGENCY = ["low", "medium", "high"]


def simple_extract(text: str) -> dict:
    """
    Extract structured information from a raw support ticket.
    This version uses simple rules so the demo stays fully free and reproducible.
    It is designed so an LLM structured-extraction layer can replace it later.
    """
    text_lower = text.lower()

    # Category logic
    if any(word in text_lower for word in ["charge", "refund", "invoice", "payment", "billed"]):
        category = "billing"
    elif any(word in text_lower for word in ["slow", "broken", "error", "can't log", "cant log", "outage", "bug"]):
        category = "bug"
    elif any(word in text_lower for word in ["would love", "feature", "add", "option", "request"]):
        category = "feature_request"
    else:
        category = "other"

    # Urgency logic
    if any(word in text_lower for word in ["refund", "can't log", "cant log", "outage", "broken", "twice"]):
        urgency = "high"
    elif any(word in text_lower for word in ["slow", "invoice", "address"]):
        urgency = "medium"
    else:
        urgency = "low"

    # Summary
    summary = text.strip()
    if len(summary) > 120:
        summary = summary[:120] + "..."

    # Recommended next action
    next_actions = {
        "billing": "Review billing records and respond within 4 hours",
        "bug": "Create engineering ticket and notify on-call if high urgency",
        "feature_request": "Log in product feedback tracker",
        "other": "Route to general support queue"
    }
    recommended_next_action = next_actions[category]

    return {
        "category": category,
        "urgency": urgency,
        "summary": summary,
        "recommended_next_action": recommended_next_action
    }


def validate_output(data: dict) -> bool:
    """Check that the extracted output follows the expected schema."""
    if data.get("category") not in CATEGORIES:
        return False
    if data.get("urgency") not in URGENCY:
        return False
    if not data.get("summary") or not data.get("recommended_next_action"):
        return False
    return True


def run_copilot(ticket_text: str) -> dict:
    """
    Main interface function.
    Takes raw ticket text and returns structured output (or an error).
    """
    result = simple_extract(ticket_text)

    if not validate_output(result):
        return {"error": "Validation failed"}

    return result


# Simple manual test (optional)
if __name__ == "__main__":
    test_ticket = "Hi, I was charged twice for my subscription this month. Can someone help me get a refund?"
    output = run_copilot(test_ticket)
    print(output)
