# ------------------------------------------------------------
# 📘 Example: Using Built-in and Custom Tools in a ReAct Agent
# ------------------------------------------------------------

from langchain.agents import Tool

# -------------------------------
# 🛠️ Define custom tools

def calculator(input_str: str) -> str:
    """A simple arithmetic calculator tool."""
    try:
        return str(eval(input_str))
    except Exception as e:
        return f"Error: {e}"

def wiki_mock(query: str) -> str:
    """A mock Wikipedia lookup for offline use."""
    data = {
        "Capital of India": "New Delhi",
        "Capital of France": "Paris"
    }
    return data.get(query, "Information not available offline.")

# -------------------------------
# 🧩 Wrap functions into LangChain Tool objects

tools = [
    Tool(
        name="Calculator",
        func=calculator,
        description="Performs basic arithmetic operations like addition or multiplication."
    ),
    Tool(
        name="Wikipedia",
        func=wiki_mock,
        description="Provides offline answers to simple knowledge queries."
    ),
]

# -------------------------------
# 🤖 Simple ReAct-style reasoning loop (offline)

def react_agent(query: str) -> str:
    """
    A lightweight, offline ReAct-style agent:
    - Identifies when to use Wikipedia or Calculator.
    - Executes tool calls.
    - Returns combined reasoning output.
    """
    response = ""
    
    # Decide when to use Wikipedia tool
    if "capital of india" in query.lower():
        obs = tools[1].func("Capital of India")
        response += f"Capital of India: {obs}\n"
        
    if "capital of france" in query.lower():
        obs = tools[1].func("Capital of France")
        response += f"Capital of France: {obs}\n"
    
    # Decide when to use Calculator tool
    import re
    calc_match = re.findall(r'(\d+\s*[\+\-\*/]\s*\d+)', query)
    for expr in calc_match:
        obs = tools[0].func(expr)
        response += f"Calculation {expr}: {obs}\n"
    
    if response == "":
        response = "No tools needed. Answer directly."
    
    return response

# -------------------------------
# 🧪 Test cases

queries = [
    "Capital of India and then calculate 25 * 4",
    "Calculate 10 + 15",
    "Capital of France and then calculate 7 * 8",
    "Who is the Prime Minister of India?"
]

for i, q in enumerate(queries, 1):
    print(f"\n✅ Test Case {i} Query: {q}")
    print(react_agent(q))
