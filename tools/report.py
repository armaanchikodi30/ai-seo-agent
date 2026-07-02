# def generate_report(
#     technical,
#     analysis,
#     competitors,
#     keywords,
#     seo,
#     score,
#     content_gap,
#     linkedin
# ):
#
#     report = f"""
#
# ======================================================================
# TECHNICAL SEO AUDIT
# ======================================================================
#
# {technical}
#
# ======================================================================
# BUSINESS ANALYSIS
# ======================================================================
#
# {analysis}
#
# ======================================================================
# COMPETITOR ANALYSIS
# ======================================================================
#
# {competitors}
#
# ======================================================================
# KEYWORD PLAN
# ======================================================================
#
# {keywords}
#
# ======================================================================
# SEO CONTENT PLAN
# ======================================================================
#
# {seo}
#
# ========================================================
# SEO SCORE DASHBOARD
# ========================================================
#
# {score}
#
# ========================================================
# CONTENT GAP ANALYSIS
# ========================================================
#
# {content_gap}
#
# ======================================================================
# LINKEDIN STRATEGY
# ======================================================================
#
# {linkedin}
#
# """
#
#     return report



def generate_report(
    technical,
    analysis,
    competitors,
    keywords,
    seo,
    score,
    content_gap,
    linkedin
):

    return {
        "technical_seo": technical,
        "business_analysis": analysis,
        "competitor_analysis": competitors,
        "keyword_plan": keywords,
        "seo_content_plan": seo,
        "seo_score_dashboard": score,
        "content_gap_analysis": content_gap,
        "linkedin_strategy": linkedin
    }