from graph import graph
from memory.memory_store import memory

def run():
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            break

        # Carrega o histórico da memória
        history = memory.load_memory_variables({"input": user_input})["history"]

        print("🧠 Current memory summary:\n", history)

        # Roda o grafo
        result = graph.invoke({
            "input": user_input,
            "history": history
        })

        print("🤖 AI:", result["output"])

        # Atualiza memória com o que o modelo respondeu
        memory.save_context({"input": user_input}, {"output": result["output"]})

if __name__ == "__main__":
    run()
