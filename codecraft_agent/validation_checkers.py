"""
Validation checkers for CodeCraft Agent.
"""

from typing import AsyncGenerator
from google.adk.agents import BaseAgent
from google.adk.events import Event, EventActions
from google.adk.agents.invocation_context import InvocationContext


class ProductOutlineValidationChecker(BaseAgent):
    """
    Ensures planner output exists.
    """

    async def _run_async_impl(self, context: InvocationContext):
        if context.session.state.get("product_outline"):
            yield Event(author=self.name, actions=EventActions(escalate=True))
        else:
            yield Event(author=self.name)


class RecommendationValidationChecker(BaseAgent):
    """
    Ensures writer output exists.
    """

    async def _run_async_impl(self, context: InvocationContext):
        if context.session.state.get("recommendation_report"):
            yield Event(author=self.name, actions=EventActions(escalate=True))
        else:
            yield Event(author=self.name)
