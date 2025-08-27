from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o")

def explain_code(state):
    question = state["input"]
    history = state.get("history", "")
    
    prompt = f"""You are a code assistant. You must explain what this code does:

Conversation so far:
{history}

Now, explain this request:
{question}
"""
    result = llm.predict(prompt)
    
    print("🧩 [explain_code] result:", result)

    return {"output": result, "history": history}
