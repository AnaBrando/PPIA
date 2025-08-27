def classify_intent(state):
    question = state["input"]

    if "test" in question.lower():
        return {"intent": "test", "input": question}
    elif "why" in question.lower() or "explain" in question.lower():
        return {"intent": "explain", "input": question}
    else:
        return {"intent": "code", "input": question}
