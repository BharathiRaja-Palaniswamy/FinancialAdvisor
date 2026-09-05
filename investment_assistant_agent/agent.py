from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from typing import Dict


investment_assistant_agent = LlmAgent(
    name="investment_assistant_agent",
    model="gemini-3.6-flash",
    description="A investment agent that guide user in stock investment.",
    instruction = """ you are a friendly investment assistant.
    you can help answer user's generic questions on stock invesment and help plan their  finance goals.  Be more friendly and positive. 
    whenever stock price is needed always fetch current data. use google search to get current stock data.
    """,
    tools=[google_search]
)

root_agent = investment_assistant_agent