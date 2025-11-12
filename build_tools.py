import requests
from pydantic import BaseModel, Field, create_model
from langchain_core.tools import StructuredTool

DEFAULT_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "DynamicToolAgent/1.0"
}

def build_tool_from_json(tool_data: dict) -> StructuredTool:
    """
    Dynamically build a StructuredTool from JSON metadata
    supporting GET, POST, PUT, DELETE methods.
    """

    # 1️⃣ Build input schema dynamically
    DynamicSchema = create_model(
        f"{tool_data['tool_name']}Input",
        **{k: (eval(v), Field(...)) for k, v in tool_data["args_schema"].items()},
        __base__=BaseModel
    )

    # 2️⃣ Build dynamic API-calling function
    def dynamic_func(**kwargs):
        method = tool_data.get("method", "GET").upper()
        url = tool_data["api_url"].format(**kwargs)
        headers = DEFAULT_HEADERS.copy()

        # Add optional headers
        if "optional_headers" in tool_data:
            for k, v in tool_data["optional_headers"].items():
                headers[k] = v

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
                "message": f"Fetched data using {kwargs}",
                "data": response.json() if response.content else {}
            }

        except requests.HTTPError as e:
            return {
                "status": "failed",
                "message": f"Request failed for {kwargs}: {str(e)}",
                "data": []
            }
        except Exception as e:
            return {
                "status": "failed",
                "message": str(e),
                "data": []
            }

    # 3️⃣ Create a uniquely named StructuredTool
    tool = StructuredTool(
        name=tool_data["tool_name"],
        description=tool_data["description"],
        args_schema=DynamicSchema,
        func=dynamic_func
    )

    return tool

