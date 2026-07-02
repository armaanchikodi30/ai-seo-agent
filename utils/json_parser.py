import json


def parse_llm_response(response):
    """
    Converts Gemini/LangChain response into a Python dictionary.
    """

    content = response.content

    # Gemini 3.x may return a list of content blocks
    if isinstance(content, list):
        text = ""

        for item in content:
            if hasattr(item, "text"):
                text += item.text
            elif isinstance(item, dict):
                text += item.get("text", "")
            else:
                text += str(item)

        content = text

    if not isinstance(content, str):
        content = str(content)

    content = (
        content.replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(content)