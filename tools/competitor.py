import json

from langchain.tools import tool
from langchain_core.prompts import PromptTemplate

from config import llm
from prompts.prompts import COMPETITOR_PROMPT
from tools.search_tool import google_search
from utils.json_parser import parse_llm_response


prompt = PromptTemplate(
    input_variables=[
        "business",
        "results"
    ],
    template=COMPETITOR_PROMPT
)


@tool
def find_competitors(business: dict) -> dict:
    """
    Find competitors using Google Search.
    """

    company = business["company_name"]
    industry = business["industry"]
    topics = business["main_topics"]

    query = f"best {industry} companies"

    if topics:
        query = f"{topics[0]} software companies"

    results = google_search.invoke(
        {
            "query": query
        }
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "business": json.dumps(business, indent=2),
            "results": results
        }
    )

    return parse_llm_response(response)