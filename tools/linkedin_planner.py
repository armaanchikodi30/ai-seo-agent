from langchain.tools import tool
from langchain_core.prompts import PromptTemplate

from config import llm
from prompts.prompts import LINKEDIN_PROMPT


prompt = PromptTemplate(
    input_variables=[
        "business",
        "seo"
    ],
    template=LINKEDIN_PROMPT
)


@tool
def generate_linkedin_strategy(
    business: str,
    seo: str
) -> str:
    """
    Generate LinkedIn content strategy.
    """

    chain = prompt | llm

    response = chain.invoke(
        {
            "business": business,
            "seo": seo
        }
    )

    return response.content