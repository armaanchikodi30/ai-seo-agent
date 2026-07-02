from langchain.tools import tool


@tool
def calculate_seo_score(
    technical: dict,
    competitors: dict,
    keywords: dict,
    seo: dict
) -> dict:
    """
    Calculates an overall SEO score based on all generated analyses.
    """

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

    if total_competitors >= 5:
        competitor_score = 90
    elif total_competitors >= 3:
        competitor_score = 80
    else:
        competitor_score = 70

    # ----------------------------
    # Keyword Score
    # ----------------------------

    keyword_score = min(
        (
            len(keywords.get("primary_keywords", [])) * 10
            + len(keywords.get("secondary_keywords", [])) * 5
        ),
        100
    )

    # ----------------------------
    # Content Score
    # ----------------------------

    content_score = min(
        (
            len(seo.get("pillar_pages", [])) * 8
            + len(seo.get("landing_pages", [])) * 6
            + len(seo.get("blog_topics", [])) * 3
            + len(seo.get("faq_topics", [])) * 2
        ),
        100
    )

    # ----------------------------
    # Overall Score
    # ----------------------------

    overall_score = round(
        (
            technical_score * 0.40
            + keyword_score * 0.20
            + content_score * 0.20
            + competitor_score * 0.20
        ),
        2
    )

    return {
        "overall_score": overall_score,
        "technical_score": technical_score,
        "content_score": content_score,
        "keyword_score": keyword_score,
        "competitor_score": competitor_score
    }