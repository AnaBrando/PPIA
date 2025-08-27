from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o")

def generate_tests(state):
    question = state["input"]
    history = state.get("history", "")

    prompt = f"""You are an expert in writing unit tests in Python.

            Conversation history:
            {history}

            Now generate Python unit tests for the following function or request:
            {question}

            Only return the test code in Python, using unittest or pytest.
            """
    result = llm.predict(prompt)

    print("🧪 [generate_tests] result:", result)

    return {"output": result, "history": history}
