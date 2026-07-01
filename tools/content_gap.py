from langchain.tools import tool
from langchain_core.prompts import PromptTemplate

from config import llm
from prompts.prompts import CONTENT_GAP_PROMPT

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
    business: str,
    competitors: str,
    keywords: str,
    seo: str
) -> str:
    """
    Compare our business with competitors and identify SEO/content gaps.
    """

    chain = prompt | llm

    response = chain.invoke(
        {
            "business": business,
            "competitors": competitors,
            "keywords": keywords,
            "seo": seo
        }
    )

    return response.content