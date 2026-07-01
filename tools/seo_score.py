import json
from langchain.tools import tool


@tool
def calculate_seo_score(
    technical: str,
    competitors: str,
    keywords: str,
    seo: str
):
    """
    Calculates an overall SEO score.
    """

    technical = json.loads(
        technical.replace("```json", "").replace("```", "")
    )

    competitors = json.loads(
        competitors.replace("```json", "").replace("```", "")
    )

    keywords = json.loads(
        keywords.replace("```json", "").replace("```", "")
    )

    seo = json.loads(
        seo.replace("```json", "").replace("```", "")
    )

    # ----------------------------
    # Technical Score
    # ----------------------------

    technical_score = technical.get("technical_score", 0)

    # ----------------------------
    # Competitor Score
    # ----------------------------

    competitor_score = 100

    total_competitors = len(
        competitors.get("competitors", [])
    )

    if total_competitors > 5:
        competitor_score = 80

    # ----------------------------
    # Keyword Score
    # ----------------------------

    keyword_score = min(
        len(keywords.get("primary_keywords", [])) * 10,
        100
    )

    # ----------------------------
    # Content Score
    # ----------------------------

    content_score = min(
        (
            len(seo.get("pillar_pages", []))
            + len(seo.get("blog_topics", []))
            + len(seo.get("faq_topics", []))
        )
        * 2,
        100
    )

    overall = round(
        (
            technical_score * 0.40
            + keyword_score * 0.20
            + content_score * 0.20
            + competitor_score * 0.20
        ),
        2,
    )

    return json.dumps(
        {
            "overall_score": overall,
            "technical_score": technical_score,
            "content_score": content_score,
            "keyword_score": keyword_score,
            "competitor_score": competitor_score,
        },
        indent=4,
    )