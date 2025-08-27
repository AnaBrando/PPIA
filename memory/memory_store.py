from langchain.memory import ConversationSummaryBufferMemory
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o")

memory = ConversationSummaryBufferMemory(
    llm=llm,
    return_messages=True,
    memory_key="history",
    input_key="input",
    max_token_limit=1000
)
