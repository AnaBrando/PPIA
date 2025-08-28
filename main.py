from graph import graph
from memory.memory_store import memory
from colorama import Fore, Style, init
import os
import time

init(autoreset=True)

def typewriter(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def run():
    clear_console()
    print(Fore.GREEN + Style.BRIGHT + "\n🌌 Welcome to the Matrix Pair Programmer.\nType something or type 'exit' to leave the simulation.\n")

    while True:
        print()  # linha extra
        user_input = input(Fore.GREEN + Style.BRIGHT + "🧑‍💻 Wake up Neo and follow the white rabbit: ")

        if user_input.lower() == "exit":
            print(Fore.RED + "\n🚪 Exiting the Matrix... Goodbye!\n")
            break

        clear_console()  # 🔥 limpa antes da IA falar

        print(Fore.YELLOW + "\n🔁 Thinking...\n")

        # Recupera histórico de memória
        history = memory.load_memory_variables({"input": user_input})["history"]

        # Executa o grafo
        result = graph.invoke({
            "input": user_input,
            "history": history
        })

        # Mostra resposta
        print(Fore.CYAN + "🤖 AI (Morpheus):", end=" ")
        typewriter(result["output"], delay=0.015)

        # Atualiza memória
        memory.save_context({"input": user_input}, {"output": result["output"]})

if __name__ == "__main__":
    run()
