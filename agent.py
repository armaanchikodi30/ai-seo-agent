import json

from tools.crawler import crawl_website
from tools.website_analyzer import analyze_business
from tools.competitor import find_competitors
from tools.keyword_planner import generate_keyword_plan
from tools.seo_planner import generate_seo_plan
from tools.linkedin_planner import generate_linkedin_strategy
from tools.report import generate_report


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
        print("Step 2 : Business Analysis...")
        print("==============================")

        business = analyze_business.invoke(
            {
                "website": website
            }
        )

        print("✓ Business Analyzed")

        print("\n==============================")
        print("Step 3 : Finding Competitors...")
        print("==============================")

        competitors = find_competitors.invoke(
            {
                "business": business
            }
        )

        print("✓ Competitors Found")

        print("\n==============================")
        print("Step 4 : Keyword Planning...")
        print("==============================")

        keywords = generate_keyword_plan.invoke(
            {
                "business": business,
                "competitors": competitors
            }
        )

        print("✓ Keyword Plan Generated")

        print("\n==============================")
        print("Step 5 : SEO Content Plan...")
        print("==============================")

        seo = generate_seo_plan.invoke(
            {
                "business": business,
                "keywords": keywords
            }
        )

        print("✓ SEO Content Plan Generated")

        print("\n==============================")
        print("Step 6 : LinkedIn Strategy...")
        print("==============================")

        linkedin = generate_linkedin_strategy.invoke(
            {
                "business": business,
                "seo": seo
            }
        )

        print("✓ LinkedIn Strategy Generated")

        report = generate_report(
            business,
            competitors,
            keywords,
            seo,
            linkedin
        )

        return report