"""
Configuration file for CodeCraft Agent.
"""

import os
from dataclasses import dataclass
import google.auth

try:
    _, project_id = google.auth.default()
    os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
except Exception:
    pass

os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")


@dataclass
class EcommerceConfiguration:
    worker_model: str = "gemini-2.5-flash"
    critic_model: str = "gemini-2.5-pro"
    max_planner_iterations: int = 3
    max_writer_iterations: int = 3


config = EcommerceConfiguration()
