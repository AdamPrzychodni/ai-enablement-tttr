import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Provide a default empty string to satisfy the type checker
    TTTR_API_KEY: str = os.getenv("TTTR_API_KEY", "") 
    TTTR_MODEL: str = os.getenv("TTTR_MODEL", "gpt-3.5-turbo-0125")
    TTTR_TEMPERATURE: float = float(os.getenv("TTTR_TEMPERATURE", 0.3))

settings = Settings()

if not settings.TTTR_API_KEY:
    raise ValueError("TTTR_API_KEY environment variable not set or empty.")
