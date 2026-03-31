
import os
from langchain.agents import initialize_agent, Tool, AgentType
from langchain_groq import ChatGroq
from langchain.utilities import WikipediaAPIWrapper

# -------------------------------
# Set Groq API key
GROQ_API_KEY = "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"

# -------------------------------
# Initialize Wikipedia API
wiki = WikipediaAPIWrapper()

def wiki_lookup(query: str) -> str:
    try:
        return wiki.run(query)
    except Exception as e:
        return f"Could not fetch information online: {e}"

# -------------------------------
# Calculator tool
def calculator(input_str: str) -> str:
    try:
        return str(eval(input_str))
    except Exception as e:
        return f"Error: {e}"

# -------------------------------
# Define tools
tools = [
    Tool(
        name="Calculator",
        func=calculator,
        description="Useful for math calculations, e.g., 25 * 4"
    ),
    Tool(
        name="Wikipedia",
        func=wiki_lookup,
        description="Fetches factual info from Wikipedia dynamically"
    )
]

# -------------------------------
# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.3,
    api_key=GROQ_API_KEY
)

# -------------------------------
# Initialize agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=1  # prevents infinite loops
)

# -------------------------------
# Interactive loop
print("Groq ReAct Agent is ready! Type your question or 'exit' to quit.")

while True:
    query = input("\n Enter Your Question: ")
    if query.lower() in ("exit", "quit"):
        print("👋 Goodbye!")
        break
    
    try:
        response = agent.invoke(query, return_intermediate_steps=False)
        print("💬 Agent:", response)
    except Exception as e:
        print("⚠️ Error:", e)
