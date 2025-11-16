from google.adk.agents import Agent

from codecraft_agent.config import config
from codecraft_agent.agent_utils import suppress_output_callback


recommendation_editor = Agent(
    model=config.critic_model,
    name="recommendation_editor",
    description="Edits the ecommerce recommendation article based on user feedback.",
    instruction="""
    You are a professional editor focused on ecommerce recommendation content.

    You will be given:
    - The current `recommendation_report` in Markdown.
    - User feedback describing what should change
      (shorter/longer, more technical, more budget-focused, simpler language, etc.).

    Your task:
    - Apply the feedback while preserving correctness and structure.
    - Improve clarity, readability, and flow.
    - Keep the output as a single Markdown article.

    Overwrite the previous article and store the updated version in `recommendation_report`.
    """,
    output_key="recommendation_report",
    after_agent_callback=suppress_output_callback,
)
