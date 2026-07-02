import json

from langchain.tools import tool
from langchain_core.prompts import PromptTemplate

from config import llm
from prompts.prompts import CONTENT_GAP_PROMPT
from utils.json_parser import parse_llm_response

prompt = PromptTemplate(
    input_variables=[
        "business",
        "competitors",
        "keywords",
        "seo"
    ],
    template=CONTENT_GAP_PROMPT
)


@tool
def generate_content_gap(
    business: dict,
    competitors: dict,
    keywords: dict,
    seo: dict
)->dict:
    """
    Compare our business with competitors and identify SEO/content gaps.
    """

    chain = prompt | llm

    response = chain.invoke(
        {
            "business": json.dumps(business, indent=2),
            "competitors": json.dumps(competitors, indent=2),
            "keywords": json.dumps(keywords, indent=2),
            "seo": json.dumps(seo, indent=2)
        }
    )

    return parse_llm_response(response)