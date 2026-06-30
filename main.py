from agent import SEOAgent


def main():

    print("=" * 70)
    print("        AI SEO AGENT USING LANGCHAIN")
    print("=" * 70)

    website = input("\nEnter Website URL : ")

    agent = SEOAgent()

    report = agent.run(website)

    print("\n")
    print("=" * 70)
    print("FINAL REPORT")
    print("=" * 70)

    print(report)


if __name__ == "__main__":
    main()