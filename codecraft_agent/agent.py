import datetime

from google.adk.agents import Agent
from google.adk.tools import FunctionTool

from codecraft_agent.config import config
from codecraft_agent.tools import fetch_products_from_category, save_recommendation_report_to_file
from codecraft_agent.sub_agents import (
    robust_product_planner,
    robust_recommendation_writer,
    recommendation_editor,
    social_media_writer
)


interactive_shopper_agent = Agent(
    name="interactive_shopper_agent",
    model=config.worker_model,
    description="Multi-agent ecommerce shopping assistant.",
    instruction=f"""
    You are CodeCraft Agent.

    Workflow:
    1. Ask user what product category they want to explore.
    2. Ask for a category URL or provide the demo URL:
       https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops
    3. Fetch products using fetch_products_from_category.
    4. Generate outline with robust_product_planner.
    5. Write recommendations with robust_recommendation_writer.
    6. Edit the article using recommendation_editor when requested.
    7. Generate social media posts with social_media_writer.
    8. Save the report using save_recommendation_report_to_file.

    If asked for your name, respond: "CodeCraft Agent".

    Current date: {datetime.datetime.now().strftime("%Y-%m-%d")}
    """,
    sub_agents=[
        robust_product_planner,
        robust_recommendation_writer,
        recommendation_editor,
        social_media_writer,
    ],
    tools=[
        FunctionTool(fetch_products_from_category),
        FunctionTool(save_recommendation_report_to_file),
    ],
    output_key="recommendation_report",
)

root_agent = interactive_shopper_agent
