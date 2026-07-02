from langchain.tools import tool
import json
from langchain_core.prompts import PromptTemplate

from config import llm
from prompts.prompts import SEO_PLAN_PROMPT

from utils.json_parser import parse_llm_response


prompt = PromptTemplate(
    input_variables=[
        "business",
        "keywords"
    ],
    template=SEO_PLAN_PROMPT
)


@tool
def generate_seo_plan(
    business: dict,
    keywords: dict
)->dict:
    """
    Generate SEO content plan.
    """

    chain = prompt | llm

    response = chain.invoke(
        {
            "business": json.dumps(business, indent=2),
            "keywords": json.dumps(keywords, indent=2)
        }
    )

    return parse_llm_response(response)