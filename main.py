from build_tools import build_tool_from_json  
from dotenv import load_dotenv
import os
from langchain_openai import AzureChatOpenAI 
from langchain.agents import create_agent
from mongodb import get_actions_collection

load_dotenv()
# JSON directly as a dictionary for demonstration

AZURE_API_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_ENDPOINT = os.getenv("ENDPOINT_URL")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME")
API_VERSION = "2025-03-01-preview"
SESSION_ID = "cli_chat_session_1"


if not all([AZURE_API_KEY, AZURE_ENDPOINT, DEPLOYMENT_NAME]):
    print("❌ ERROR: Missing required environment variables (AZURE_OPENAI_KEY, ENDPOINT_URL, or DEPLOYMENT_NAME).")
    exit()

try:
    llm = AzureChatOpenAI(
        azure_endpoint=AZURE_ENDPOINT,
        openai_api_key=AZURE_API_KEY,
        openai_api_version=API_VERSION,
        azure_deployment=DEPLOYMENT_NAME,
        temperature=0.7,
    )
    print("✅ AzureChatOpenAI initialized successfully.")
except Exception as e:
    print(f"❌ Error initializing AzureChatOpenAI: {e}")
    print("Hint: Please check endpoint, deployment name, and API_VERSION in Azure portal.")
    exit()

from uuid import UUID
from build_tools import build_tool_from_json
from mongodb import get_actions_collection

def create_tool_retriever(tenant_id_input: str):
    # 1️⃣ Convert tenant input → proper UUID()
    tenant_uuid = UUID(tenant_id_input)

    # 2️⃣ Correct MongoDB query
    pre_filter_query = {"tenantId": tenant_uuid}

    # 3️⃣ Fetch and convert tools
    collection = get_actions_collection()
    tool_docs = list(collection.find(pre_filter_query))
    
    return [build_tool_from_json(doc) for doc in tool_docs]


# 🔥 You only give the tenantId string here
actions_retrived = create_tool_retriever(
    "021ee120-7cc2-4f78-9ff5-db9e785c0118"
)

agent = create_agent(
    model=llm,
    tools=actions_retrived,
    system_prompt=(
        "You are an intelligent API orchestration agent. "
        "Your job is to understand the user's natural language requests, "
        "select the most relevant tool from the provided list, "
        "and execute it with the correct input arguments. "
        "Each tool represents an API endpoint with specific parameters. "
        "Always extract parameter values from the user query, call the right tool, "
        "and return only the JSON or API response in a clear format. "
        "Do not make assumptions or fabricate data. "
        "Do not generate answers from your own knowledge or reasoning. "
        "Only respond with data obtained from the tool responses. "
        "If the tool requires authentication, mention that a token is needed. "
        "If the requested information cannot be found using the available tools, "
        "respond exactly with: 'I am sorry, I could not find the answer.'"
    ),
)

print(agent.invoke({
    "messages": [
        {"role": "user", "content": "Fetch post 10 from jsonplaceholder"}
    ]
}))



