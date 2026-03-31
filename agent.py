from langchain.agents import Tool

# -------------------------------
# Define tools

def calculator(input_str: str) -> str:
    try:
        return str(eval(input_str))
    except Exception as e:
        return f"Error: {e}"

def wiki_mock(query: str) -> str:
    data = {
        "Capital of India": "New Delhi",
        "Capital of France": "Paris"
    }
    return data.get(query, "Information not available offline.")

tools = {
    "Calculator": calculator,
    "Wikipedia": wiki_mock
}

# -------------------------------
# Simple offline ReAct simulation

def react_agent(query: str) -> str:
    response = ""
    
    if "capital of india" in query.lower():
        obs = tools["Wikipedia"]("Capital of India")
        response += f"Capital of India: {obs}\n"
        
    if "capital of france" in query.lower():
        obs = tools["Wikipedia"]("Capital of France")
        response += f"Capital of France: {obs}\n"
        
    import re
    calc_match = re.findall(r'(\d+\s*[\+\-\*/]\s*\d+)', query)
    for expr in calc_match:
        obs = tools["Calculator"](expr)
        response += f"Calculation {expr}: {obs}\n"
    
    if response == "":
        response = "No tools needed. Answer directly."
    
    return response

# -------------------------------
# Test cases

queries = [
    "Capital of India and then calculate 25 * 4",
    "Calculate 10 + 15",
    "Capital of France and then calculate 7 * 8"
]

for i, q in enumerate(queries, 1):
    print(f"\n✅ Test Case {i} Response:")
    print(react_agent(q)) 
