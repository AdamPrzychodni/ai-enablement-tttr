import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Settings:
    """
    Configuration settings for the application.
    Reads from environment variables.
    """
    TTTR_API_KEY: str = os.getenv("TTTR_API_KEY", "")
    TTTR_MODEL: str = os.getenv("TTTR_MODEL", "gpt-4")
    TTTR_TEMPERATURE: float = float(os.getenv("TTTR_TEMPERATURE", 0.7))

settings = Settings()

# Raise an error if the API key is not set
if not settings.TTTR_API_KEY:
    raise ValueError("TTTR_API_KEY environment variable not set. Please add it to your .env file.")