from codecraft_agent.sub_agents.product_scanner import ProductScannerAgent
from codecraft_agent.sub_agents.spec_analyzer import SpecAnalyzerAgent
from codecraft_agent.sub_agents.sentiment_agent import SentimentAgent
from codecraft_agent.sub_agents.ranking_agent import RankingAgent
from codecraft_agent.sub_agents.summary_writer import SummaryWriterAgent

class ShopperOrchestrator:
    def __init__(self):
        self.product_scanner = ProductScannerAgent()
        self.spec_analyzer = SpecAnalyzerAgent()
        self.sentiment_agent = SentimentAgent()
        self.ranking_agent = RankingAgent()
        self.summary_writer = SummaryWriterAgent()

    def run(self, url: str):
        # Step 1: scrape products
        products = self.product_scanner.run(url)

        # Step 2: analyze specs
        self.spec_analyzer.run(products)

        # Step 3: sentiment analysis
        self.sentiment_agent.run(products)

        # Step 4: ranking
        ranked_products = self.ranking_agent.run(products)

        # Step 5: summary report
        summary = self.summary_writer.run(ranked_products)

        return {
            "ranked_products": ranked_products,
            "summary": summary
        }
