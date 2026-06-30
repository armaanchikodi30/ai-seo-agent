import json

from langchain.tools import tool
from langchain_core.prompts import PromptTemplate

from config import llm
from prompts.prompts import KEYWORD_PLAN_PROMPT


prompt = PromptTemplate(
    input_variables=[
        "business",
        "competitors"
    ],
    template=KEYWORD_PLAN_PROMPT
)


@tool
def generate_keyword_plan(
    business: str,
    competitors: str
) -> str:
    """
    Generate SEO keyword strategy.
    """

    chain = prompt | llm

    response = chain.invoke(
        {
            "business": business,
            "competitors": competitors
        }
    )

    return response.content