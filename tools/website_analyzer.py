from langchain.tools import tool
from langchain_core.prompts import PromptTemplate

from config import llm
from prompts.prompts import BUSINESS_ANALYSIS_PROMPT

from utils.json_parser import parse_llm_response


prompt = PromptTemplate(
    input_variables=["website"],
    template=BUSINESS_ANALYSIS_PROMPT
)


@tool
def analyze_business(website: str) -> dict:
    """
    Analyze the crawled website and understand the business.
    """

    chain = prompt | llm

    response = chain.invoke(
        {
            "website": website
        }
    )

    return parse_llm_response(response)