from langchain.tools import tool
from langchain_core.prompts import PromptTemplate
import json
from config import llm
from prompts.prompts import LINKEDIN_PROMPT
from utils.json_parser import parse_llm_response

prompt = PromptTemplate(
    input_variables=[
        "business",
        "seo"
    ],
    template=LINKEDIN_PROMPT
)


@tool
def generate_linkedin_strategy(
    business: dict,
    seo: dict
)->dict:
    """
    Generate LinkedIn content strategy.
    """

    chain = prompt | llm

    response = chain.invoke(
        {
            "business": json.dumps(business, indent=2),
            "seo": json.dumps(seo, indent=2)
        }
    )

    return parse_llm_response(response)