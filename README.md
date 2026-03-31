# ReAct Agent (Groq API)

This project is a simple implementation of a ReAct-style AI agent built using Python and the Groq API. The goal of this project was to understand how modern AI agents reason through problems step-by-step and interact with tools, instead of just returning direct answers.

Rather than focusing on a complex UI, this project keeps things minimal and focuses on the core idea: **reasoning + action**.

---

## What this project does

- Takes a user query as input
- Breaks it down into reasoning steps
- Decides what action to take
- Executes the action and returns a response

It follows the ReAct pattern (Thought → Action → Observation), which is commonly used in modern AI agent systems.

---

## Tech used

- Python
- Groq API
- LangChain (for agent structure)
- dotenv (for managing API keys)

---

## Project structure
```plaintext
ReAct_agent/
│
├── react_groq_agent.py   # Main agent logic
├── requirements.txt      # Dependencies
├── README.md
├── .env                  # Not included in repo
└── .gitignore``` 
---

## How to run
1. Clone the repository 
```bash
git clone https://github.com/shripatil70/ReAct_agent.git 
dd ReAct_agent 
```
2. Create and activate virtual environment 
```bash 
pip -m venv venv 
v v\Scripts\activate 
```
3. Install dependencies 
```bash 
pip install -r requirements.txt 
```
4. Create a `.env` file and add your API key 
```bash 
GROQ_API_KEY=your_api_key_here 
```
5. Run the project 
```bash 
python react_groq_agent.py 
```
---
## Why I built this
I built this project to explore how AI agents work beyond basic prompt-response systems. Most tutorials stop at simple chatbots, but I wanted to understand how agents can **think, decide, and act** in a more structured way.
This project helped me get hands-on experience with:
- Agent workflows
- API integration
- Structuring AI logic in Python  
---
## Possible improvements  
e.g., Add a frontend (React-based UI), Integrate external tools (search, APIs), Add memory for multi-step conversations, Deploy as a web app  
---
## Note  The `.env` file is not included for security reasons. Make sure to add your own API key before running the project.
---
## Author  Dhanashri Patil
