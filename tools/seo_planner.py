from langchain.tools import tool
from langchain_core.prompts import PromptTemplate

from config import llm
from prompts.prompts import SEO_PLAN_PROMPT


prompt = PromptTemplate(
    input_variables=[
        "business",
        "keywords"
    ],
    template=SEO_PLAN_PROMPT
)


@tool
def generate_seo_plan(
    business: str,
    keywords: str
) -> str:
    """
    Generate SEO content plan.
    """

    chain = prompt | llm

    response = chain.invoke(
        {
            "business": business,
            "keywords": keywords
        }
    )

    return response.content