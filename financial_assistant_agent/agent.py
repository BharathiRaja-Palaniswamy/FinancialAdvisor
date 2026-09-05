from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from investment_assistant_agent.agent import investment_assistant_agent
from typing import Dict

def get_user_personal_financial_details() -> Dict:
    """
    Gets users personal finance details like salary, expense and savings capacity.
    """
    return {
        "salary": 50000,
        "expense": {
            "emi": 5000,
            "fuel": 1000,
            "shopping": 20000
        },
        "savings": 10000
    }
financial_assistant_agent = LlmAgent(
    name="financial_assistant_agent",
    model="gemini-3.6-flash",
    description="A financial assistant that helps with user's financial goals",
    instruction = """ you are a friendly finance assistant.
    you can help answer user's generic questions on finance and help plan their  finance goals.  Be more friendly and positive.
    you have two tools to complete the task.
    use get_user_personal_financial_details to fetch user financial details.
    user investment_assistant_agent to fetch data related to investment like stock price, stock market data.
    
    """,
    tools=[AgentTool(investment_assistant_agent),get_user_personal_financial_details]
)

root_agent = financial_assistant_agent