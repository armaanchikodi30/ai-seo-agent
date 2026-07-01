from langchain.tools import tool
from langchain_core.prompts import PromptTemplate

from config import llm
from prompts.prompts import TECHNICAL_SEO_PROMPT


prompt = PromptTemplate(
    input_variables=["website"],
    template=TECHNICAL_SEO_PROMPT
)


@tool
def technical_seo_audit(website: str) -> str:
    """
    Performs a complete technical SEO audit.
    """

    chain = prompt | llm

    response = chain.invoke(
        {
            "website": website
        }
    )

    return response.content