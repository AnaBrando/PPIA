from langgraph.graph import StateGraph
from nodes.classify_intent import classify_intent
from nodes.generate_code import generate_code
from nodes.explain_code import explain_code
from nodes.generate_tests import generate_tests

from typing import TypedDict

# Define o formato do estado que circula entre os nós
class State(TypedDict):
    input: str
    history: str
    output: str

builder = StateGraph(State)

# Define states
builder.add_node("ClassifyIntent", classify_intent)
builder.add_node("GenerateCode", generate_code)
builder.add_node("ExplainCode", explain_code)
builder.add_node("GenerateTests", generate_tests)

# Transitions
builder.set_entry_point("ClassifyIntent")
builder.add_conditional_edges("ClassifyIntent", lambda x: x["intent"], {
    "code": "GenerateCode",
    "explain": "ExplainCode",
    "test": "GenerateTests",
})


builder.set_finish_point("GenerateCode")
builder.set_finish_point("ExplainCode")
builder.set_finish_point("GenerateTests")

graph = builder.compile()
