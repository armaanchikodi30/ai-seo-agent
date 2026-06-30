import requests

from bs4 import BeautifulSoup
from langchain.tools import tool


@tool
def crawl_website(url: str) -> str:
    """
    Crawl a website and extract important SEO content.
    """

    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=20
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "lxml"
    )

    title = soup.title.text if soup.title else ""

    meta = soup.find(
        "meta",
        attrs={"name": "description"}
    )

    description = ""

    if meta:
        description = meta.get(
            "content",
            ""
        )

    headings = []

    for tag in soup.find_all(
        ["h1", "h2"]
    ):
        headings.append(
            tag.get_text(
                " ",
                strip=True
            )
        )

    paragraphs = []

    for p in soup.find_all("p"):

        text = p.get_text(
            " ",
            strip=True
        )

        if len(text) > 50:
            paragraphs.append(text)

    return f"""
Title:

{title}

Description:

{description}

Headings:

{headings}

Content:

{' '.join(paragraphs[:20])}
"""