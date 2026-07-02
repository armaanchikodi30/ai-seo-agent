import json

from langchain.tools import tool
from langchain_core.prompts import PromptTemplate

from config import llm
from prompts.prompts import KEYWORD_PLAN_PROMPT
from utils.json_parser import parse_llm_response

prompt = PromptTemplate(
    input_variables=[
        "business",
        "competitors"
    ],
    template=KEYWORD_PLAN_PROMPT
)


@tool
def generate_keyword_plan(
    business: dict,
    competitors: dict
)->dict:
    """
    Generate SEO keyword strategy.
    """

    chain = prompt | llm

    response = chain.invoke(
        {
            "business": json.dumps(business, indent=2),
            "competitors": json.dumps(competitors, indent=2)
        }
    )

    return parse_llm_response(response)