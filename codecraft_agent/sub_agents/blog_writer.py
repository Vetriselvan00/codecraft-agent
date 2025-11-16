from google.adk.agents import Agent, LoopAgent
from google.adk.tools import google_search

from codecraft_agent.config import config
from codecraft_agent.validation_checkers import RecommendationValidationChecker
from codecraft_agent.agent_utils import suppress_output_callback


blog_writer = Agent(
    model=config.critic_model,
    name="recommendation_writer",
    description="Writes a full ecommerce recommendation article.",
    instruction="""
    You are an expert ecommerce reviewer.

    You will be given:
    - `product_outline` in Markdown (how to structure the article).
    - `products` list in session.state:
      [{name, price, rating, description, url}, ...]
    - User preferences (budget, performance vs portability, etc.).

    Your job:
    - Follow the outline to write a full recommendation article in Markdown.
    - Explain clearly why some products are "Best Overall", "Best Budget",
      "Best Premium", etc.
    - Highlight both pros and cons honestly.
    - Use Google Search only for general background (e.g., typical spec ranges),
      not for scraping live product pages.

    Structure suggestion:
    - Title
    - Short introduction
    - One section per group (Best Overall, Best Budget, etc.)
    - Comparison notes
    - Final summary with bullet-point shortlist

    Do NOT wrap the entire article in a single code block.
    Write plain Markdown and store it in `recommendation_report`.
    """,
    tools=[google_search],
    output_key="recommendation_report",
    after_agent_callback=suppress_output_callback,
)

robust_recommendation_writer = LoopAgent(
    name="robust_recommendation_writer",
    description="Retries article writer until a valid recommendation report exists.",
    sub_agents=[
        blog_writer,
        RecommendationValidationChecker(name="recommendation_validation_checker"),
    ],
    max_iterations=config.max_writer_iterations,
)
