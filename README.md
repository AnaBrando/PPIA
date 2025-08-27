# 🤖 AI Pair Programmer – Python + LangGraph + GPT-4o

This is an experimental project that simulates an intelligent **pair programming assistant** using Python, OpenAI, and LangGraph.

The AI is capable of:
- ✅ Detecting the user’s intent (e.g., generate, explain, or test code)
- 💡 Suggesting Python code solutions
- 🧠 Explaining code step by step
- 🧪 Generating unit test examples
- 🔁 Maintaining memory of reasoning across turns

---

## 🧠 Architecture

This project uses **LangGraph** to define a state machine with the following flow:

```
input → ClassifyIntent → [GenerateCode | ExplainCode | GenerateTests] → END
```

Each user input is classified and routed to the proper handler.

---

## 💻 Technologies Used

- Python 3.11+
- LangChain
- LangGraph
- langchain-openai
- OpenAI GPT-4o
- ConversationSummaryBufferMemory

---

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-pair-programmer-python.git
   cd ai-pair-programmer-python
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key as an environment variable:
   ```bash
   export OPENAI_API_KEY=sk-xxxxx  # Linux/macOS
   set OPENAI_API_KEY=sk-xxxxx     # Windows
   ```

4. Run the project:
   ```bash
   python main.py
   ```

---

## 🧪 Example Interaction

```bash
You: Create a function that reverses a string
🤖 AI:
def reverse(text):
    return text[::-1]
```

```bash
You: Explain it to me
🤖 AI:
This function uses Python slicing with a step of -1 to reverse the characters.
```

```bash
You: Give me a test for it
🤖 AI:
def test_reverse():
    assert reverse("abc") == "cba"
```

---

## 📂 Project Structure

```
📁 ai_pair_programmer/
├── main.py
├── graph.py
├── memory_store.py
└── nodes/
    ├── classify_intent.py
    ├── generate_code.py
    ├── explain_code.py
    └── generate_tests.py
```

---

## 💡 Future Ideas

- Continuous chat with LangGraph loops
- Web UI (e.g., Streamlit) for interactive coding
- Secure code execution (sandboxed)
- Automatic GitHub PR code review comments

---

## 🧑‍💻 Developed by

**Ana Paula Chaves**  
Senior Software Engineer – Investment Division @ Itaú Unibanco

🔗 [LinkedIn](https://www.linkedin.com/in/anachavesdev/)  
🔗 [GitHub](https://github.com/AnaBrando)