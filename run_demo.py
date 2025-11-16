from codecraft_agent.orchestrator import ShopperOrchestrator

DEFAULT_URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

def main():
    print("=== CodeCraft Agent – Demo Run ===")
    orchestrator = ShopperOrchestrator()
    result = orchestrator.run(DEFAULT_URL)

    print("\n=== Top Recommendations ===")
    for i, product in enumerate(result["ranked_products"][:5], start=1):
        print(f"{i}. {product.name} - ${product.price:.2f} (score={product.score:.2f})")

    with open("recommendations.md", "w", encoding="utf-8") as f:
        f.write(result["summary"])

    print("\nSaved to recommendations.md")

if __name__ == "__main__":
    main()
