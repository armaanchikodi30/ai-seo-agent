BUSINESS_ANALYSIS_PROMPT = """
You are an expert SEO consultant.

Analyze the following website and understand the business in depth.

Return ONLY valid JSON.

{{
    "company_name":"",
    "website":"",
    "industry":"",
    "business_summary":"",
    "products":[],
    "services":[],
    "unique_selling_points":[],
    "target_audience":[],
    "business_goals":[],
    "main_topics":[],
    "primary_keywords":[],
    "brand_tone":"",
    "value_proposition":""
}}

Website Content:

{website}
"""


COMPETITOR_PROMPT = """
You are an experienced SEO and Competitive Intelligence expert.

Identify the top 5 real competitors based on the business information and search results.

Business:

{business}

Google Search Results:

{results}

For each competitor provide:

- Company Name
- Website
- Business Summary
- Why they are a competitor
- Products / Services
- Target Audience
- Unique Selling Points
- SEO Strengths
- Content Strategy
- Weaknesses
- Missing Opportunities
- Recommendations

Return ONLY valid JSON.

{{
    "competitors":[
        {{
            "company_name":"",
            "website":"",
            "business_summary":"",
            "why_competitor":"",
            "products_services":[],
            "target_audience":[],
            "unique_selling_points":[],
            "seo_strengths":[],
            "content_strategy":"",
            "weaknesses":[],
            "missing_opportunities":[],
            "recommendations":[]
        }}
    ]
}}
"""


KEYWORD_PLAN_PROMPT = """
You are an SEO Strategist.

Using the business information and competitor analysis, generate a comprehensive keyword strategy.

Business:

{business}

Competitors:

{competitors}

Return ONLY valid JSON.

{{
    "primary_keywords":[],
    "secondary_keywords":[],
    "long_tail_keywords":[],
    "transactional_keywords":[],
    "informational_keywords":[],
    "local_keywords":[],
    "high_intent_keywords":[],
    "competitor_keywords":[]
}}
"""


SEO_PLAN_PROMPT = """
You are an SEO Content Strategist.

Using the business information and keyword strategy, create a complete SEO roadmap.

Business:

{business}

Keywords:

{keywords}

Return ONLY valid JSON.

{{
    "pillar_pages":[],
    "landing_pages":[],
    "blog_topics":[],
    "faq_topics":[],
    "content_clusters":[],
    "internal_linking_strategy":[],
    "schema_recommendations":[],
    "meta_title_suggestions":[],
    "meta_description_suggestions":[]
}}
"""


LINKEDIN_PROMPT = """
You are a LinkedIn Marketing Strategist.

Generate a complete 30-day LinkedIn content calendar.

Business:

{business}

SEO Plan:

{seo}

Return ONLY valid JSON.

{{
    "week1":[],
    "week2":[],
    "week3":[],
    "week4":[]
}}
"""


TECHNICAL_SEO_PROMPT = """
You are a Senior Technical SEO Consultant.

Analyze the crawled website information.

Evaluate:

- Page Title
- Meta Description
- Heading Structure
- Images
- Robots.txt
- XML Sitemap
- HTTPS
- Canonical Tags
- Internal Links
- External Links

Return ONLY valid JSON.

{{
    "technical_score":0,

    "page_title":{{
        "status":"",
        "remarks":""
    }},

    "meta_description":{{
        "status":"",
        "remarks":""
    }},

    "headings":{{
        "status":"",
        "remarks":""
    }},

    "images":{{
        "status":"",
        "total_images":0,
        "missing_alt":0,
        "remarks":""
    }},

    "robots_txt":{{
        "status":"",
        "remarks":""
    }},

    "sitemap":{{
        "status":"",
        "remarks":""
    }},

    "https":{{
        "status":"",
        "remarks":""
    }},

    "canonical":{{
        "status":"",
        "remarks":""
    }},

    "internal_links":{{
        "status":"",
        "remarks":""
    }},

    "external_links":{{
        "status":"",
        "remarks":""
    }},

    "recommendations":[]
}}

Website Content:

{website}
"""


CONTENT_GAP_PROMPT = """
You are an expert SEO consultant.

Compare our business with the competitors and identify opportunities.

Business:

{business}

Competitors:

{competitors}

Keywords:

{keywords}

SEO Plan:

{seo}

Return ONLY valid JSON.

{{
    "missing_services":[],
    "missing_pages":[],
    "missing_keywords":[],
    "missing_blog_topics":[],
    "content_opportunities":[],
    "seo_opportunities":[],
    "recommendations":[]
}}
"""