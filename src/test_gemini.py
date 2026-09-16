import os

from dotenv import load_dotenv
from crewai import LLM


# Load variables from .env
load_dotenv()


# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")


# Check API key
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY is missing. "
        "Please add it to your .env file."
    )


# Create Gemini LLM
llm = LLM(
    model="gemini/gemini-3.6-flash",
    api_key=api_key,
    temperature=0.7
)


# Send a simple prompt
response = llm.call(
    "Write one professional sentence greeting a professor."
)


print("\nGemini Response:")
print(response)