from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o")

def generate_code(state):
    question = state["input"]
    history = state.get("history", "")
    
    print("🧩 [generate_code] question:", question)
    print("🧩 [generate_code] history:", history)
    
    prompt = f"""You are a helpful AI pair programmer.
You have the following conversation history:
{history}

Now help with: {question}
"""
    result = llm.predict(prompt)
    
    print("🧩 [generate_code] result:", result)

    return {"output": result, "history": history}
