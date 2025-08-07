# agent/setup.py

import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from .triage_agent import triage_agent
from dataclasses import dataclass

# Load env vars
load_dotenv()

# Global context class
@dataclass
class AppContext:
    token = None
    name = None
    email = None
    password = None

# Gemini setup
gemini_api_key = os.getenv("API_KEY")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)

__all__ = ["AppContext", "config", "triage_agent"]
