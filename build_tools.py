import requests
from pydantic import BaseModel, Field, create_model
from langchain_core.tools import StructuredTool
import re 

DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "DynamicToolAgent/1.0"
}
def sanitize_tool_name(name: str) -> str:
    """Replace invalid characters with underscore."""
    return re.sub(r'[^a-zA-Z0-9_\.-]', '_', name)

def build_tool_from_json(tool_data: dict) -> StructuredTool:
    """
    Build a StructuredTool from MongoDB-style JSON.
    """

    
    tool_name = sanitize_tool_name(tool_data['name'])
    print("Building tool:", tool_name)
    # -------------------------------
    # 1️⃣ Convert parameters (list → dict)
    # -------------------------------
    params_dict = {}

    for p in tool_data.get("parameters", []):
        field_name = p.get("name")
        field_type = p.get("type", "str")
        python_type = eval(field_type)  # safe since types are basic
        
        params_dict[field_name] = (python_type, Field(...))

    DynamicSchema = create_model(
        f"{tool_data['name']}Input",
        **params_dict,
        __base__=BaseModel
    )

    # -------------------------------
    # 2️⃣ Convert headers list → dict
    # -------------------------------
    extra_headers = {}
    for h in tool_data.get("headers", []):
        extra_headers[h["key"]] = h["value"]

    # -------------------------------
    # 3️⃣ Dynamic API-call function
    # -------------------------------
    def dynamic_func(**kwargs):
        method = tool_data.get("httpMethod", "GET").upper()
        url = tool_data.get("url", "").format(**kwargs)

        headers = DEFAULT_HEADERS.copy()
        headers.update(extra_headers)

        try:
            if method == "GET":
                response = requests.get(url, headers=headers, params=kwargs)

            elif method == "POST":
                response = requests.post(url, headers=headers, json=kwargs)

            elif method == "PUT":
                response = requests.put(url, headers=headers, json=kwargs)

            elif method == "DELETE":
                response = requests.delete(url, headers=headers, json=kwargs)

            else:
                return {
                    "status": "failed",
                    "message": f"Unsupported HTTP method: {method}",
                    "data": []
                }

            response.raise_for_status()

            return {
                "status": "success",
                "message": f"Success {kwargs}",
                "data": response.json() if response.content else {}
            }

        except Exception as e:
            return {
                "status": "failed",
                "message": str(e),
                "data": []
            }

    # -------------------------------
    # 4️⃣ Build Tool
    # -------------------------------
    tool = StructuredTool(
        name=tool_name,  
        description=tool_data.get("description", ""),
        args_schema=DynamicSchema,
        func=dynamic_func
    )

    return tool
