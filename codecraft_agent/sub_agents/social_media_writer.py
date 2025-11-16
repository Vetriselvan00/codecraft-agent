from google.adk.agents import Agent

from codecraft_agent.config import config


social_media_writer = Agent(
    model=config.critic_model,
    name="social_media_writer",
    description="Writes social media posts to promote the ecommerce recommendations.",
    instruction="""
    You are a social media marketing expert for ecommerce.

    Input:
    - The final `recommendation_report` (Markdown) that summarizes
      recommended products for a certain category.

    Output:
    - One Twitter/X post (max ~280 characters, engaging, with 1–3 relevant hashtags).
    - One LinkedIn post (more detailed, professional, value-focused).

    Format your response as Markdown:

    ### Twitter

    ```
    <twitter_post_here>
    ```

    ### LinkedIn

    ```
    <linkedin_post_here>
    ```

    Store this entire Markdown snippet in `social_media_posts`.
    """,
    output_key="social_media_posts",
)

