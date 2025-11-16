from google.adk.agents import Agent, LoopAgent
from google.adk.tools import google_search

from codecraft_agent.config import config
from codecraft_agent.validation_checkers import ProductOutlineValidationChecker
from codecraft_agent.agent_utils import suppress_output_callback


blog_planner = Agent(
    model=config.worker_model,
    name="product_planner",
    description="Creates a comparison outline for ecommerce products.",
    instruction="""
    You are an ecommerce strategist.

    Input:
    - A list of 'products' in session.state (each with name, price, rating, description, url).
    - The user's product category and preferences.

    Task:
    - Examine the products and think like a smart shopper.
    - Decide 3–7 key comparison criteria (e.g., price, performance, battery life,
      build quality, features, warranty, brand trust).
    - Group products logically (e.g., Best Budget, Best Overall, Best Premium).
    - Produce a clear Markdown outline describing sections and comparison points.

    Output:
    - Save the Markdown outline into the `product_outline` state key.
    """,
    tools=[google_search],
    output_key="product_outline",
    after_agent_callback=suppress_output_callback,
)

robust_product_planner = LoopAgent(
    name="robust_product_planner",
    description="Retries product planner until a valid outline is created.",
    sub_agents=[
        blog_planner,
        ProductOutlineValidationChecker(name="product_outline_validation_checker"),
    ],
    max_iterations=config.max_planner_iterations,
    after_agent_callback=suppress_output_callback,
)
