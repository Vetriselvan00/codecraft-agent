"""
Utility callbacks for CodeCraft Agent.
"""

from google.adk.agents.callback_context import CallbackContext
from google.genai.types import Content


def suppress_output_callback(callback_context: CallbackContext) -> Content:
    """
    Suppress visible model output for intermediate agents.
    Keeps conversation clean and readable.
    """
    return Content()
