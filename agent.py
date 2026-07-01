import json

from tools.crawler import crawl_website
from tools.website_analyzer import analyze_business
from tools.competitor import find_competitors
from tools.keyword_planner import generate_keyword_plan
from tools.seo_planner import generate_seo_plan
from tools.linkedin_planner import generate_linkedin_strategy
from tools.report import generate_report
from tools.technical_seo import technical_seo_audit
from tools.seo_score import calculate_seo_score
from tools.content_gap import generate_content_gap

class SEOAgent:

    def __init__(self):
        pass

    def run(self, website_url: str):

        print("\n==============================")
        print("Step 1 : Crawling Website...")
        print("==============================")

        website = crawl_website.invoke(
            {
                "url": website_url
            }
        )

        print("✓ Website Crawled")

        print("\n==============================")
        print("Step 2 : Technical SEO Audit...")
        print("==============================")

        technical = technical_seo_audit.invoke(
            {
                "website": website
            }
        )

        print("✓ Technical SEO Audit Completed")

        print("\n==============================")
        print("Step 3 : Business Analysis...")
        print("==============================")

        business = analyze_business.invoke(
            {
                "website": website
            }
        )

        print("✓ Business Analyzed")

        print("\n==============================")
        print("Step 4 : Finding Competitors...")
        print("==============================")

        competitors = find_competitors.invoke(
            {
                "business": business
            }
        )

        print("✓ Competitors Found")

        print("\n==============================")
        print("Step 5 : Keyword Planning...")
        print("==============================")

        keywords = generate_keyword_plan.invoke(
            {
                "business": business,
                "competitors": competitors
            }
        )

        print("✓ Keyword Plan Generated")

        print("\n==============================")
        print("Step 6 : SEO Content Plan...")
        print("==============================")

        seo = generate_seo_plan.invoke(
            {
                "business": business,
                "keywords": keywords
            }
        )

        print("✓ SEO Content Plan Generated")

        print("\n==============================")
        print("Step 7 : Content Gap Analysis...")
        print("==============================")

        content_gap = generate_content_gap.invoke(
            {
                "business": business,
                "competitors": competitors,
                "keywords": keywords,
                "seo": seo
            }
        )

        print("✓ Content Gap Analysis Completed")

        print("\n==============================")
        print("Step 8 : SEO Score Dashboard...")
        print("==============================")

        score = calculate_seo_score.invoke(
            {
                "technical": technical,
                "competitors": competitors,
                "keywords": keywords,
                "seo": seo
            }
        )

        print("✓ SEO Score Generated")

        print("\n==============================")
        print("Step 9 : LinkedIn Strategy...")
        print("==============================")

        linkedin = generate_linkedin_strategy.invoke(
            {
                "business": business,
                "seo": seo
            }
        )

        print("✓ LinkedIn Strategy Generated")

        report = generate_report(
            technical,
            business,
            competitors,
            keywords,
            seo,
            score,
            content_gap,
            linkedin
        )

        return report