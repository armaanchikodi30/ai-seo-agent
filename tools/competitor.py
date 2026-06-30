import json

from langchain.tools import tool

from tools.search_tool import google_search

from config import llm

from langchain_core.prompts import PromptTemplate

from prompts.prompts import COMPETITOR_PROMPT


prompt = PromptTemplate(
    input_variables=[
        "business",
        "results"
    ],
    template=COMPETITOR_PROMPT
)


@tool
def find_competitors(business: str) -> str:
    """
    Find competitors using Google Search.
    """

    business_json = json.loads(
        business.replace("```json", "").replace("```", "")
    )

    company = business_json["company_name"]

    industry = business_json["industry"]

    topics = business_json["main_topics"]

    query = f"best {industry} companies"

    if len(topics):

        query = f"{topics[0]} software companies"

    results = google_search.invoke(
        {
            "query": query
        }
    )

    chain = prompt | llm

    response = chain.invoke(
        {
            "business": business,
            "results": results
        }
    )

    return response.content