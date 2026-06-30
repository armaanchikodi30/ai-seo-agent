import requests

from langchain.tools import tool

from config import ZENSERP_API_KEY


@tool
def google_search(query: str) -> str:
    """
    Search Google using Zenserp.
    Returns the first 10 organic search results.
    """

    url = "https://app.zenserp.com/api/v2/search"

    headers = {
        "apikey": ZENSERP_API_KEY
    }

    params = {
        "q": query,
        "hl": "en",
        "gl": "us"
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    results = []

    organic = data.get("organic", [])

    for item in organic[:10]:

        results.append(
            {
                "title": item.get("title", ""),
                "url": item.get("url", ""),
                "description": item.get("description", "")
            }
        )

    return str(results)