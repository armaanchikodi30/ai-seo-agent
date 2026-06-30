BUSINESS_ANALYSIS_PROMPT = """
You are an expert SEO consultant.

Analyze the following website content.

Return ONLY valid JSON.

The response should contain:

{{
    "company_name":"",
    "industry":"",
    "business_summary":"",
    "products":[],
    "target_audience":[],
    "main_topics":[]
}}

Website Content:

{website}
"""


COMPETITOR_PROMPT = """
You are an SEO expert.

Given the following business information and Google search results,
identify ONLY real competitors.

Business:

{business}

Search Results:

{results}

Return ONLY JSON.

{{
    "competitors":[]
}}
"""


KEYWORD_PLAN_PROMPT = """
You are an SEO Strategist.

Using the business details and competitors,
generate a keyword plan.

Business:

{business}

Competitors:

{competitors}

Return JSON.

{{
    "primary_keywords":[],
    "secondary_keywords":[],
    "long_tail_keywords":[]
}}
"""


SEO_PLAN_PROMPT = """
Create an SEO content strategy.

Business:

{business}

Keywords:

{keywords}

Return JSON.

{{
    "pillar_pages":[],
    "blog_topics":[],
    "faq_topics":[]
}}
"""


LINKEDIN_PROMPT = """
Create a 30-day LinkedIn content strategy.

Business:

{business}

SEO Plan:

{seo}

Return JSON.

{{
    "week1":[],
    "week2":[],
    "week3":[],
    "week4":[]
}}
"""