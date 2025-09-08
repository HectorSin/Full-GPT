import os
from dotenv import load_dotenv


def get_env():
    load_dotenv(dotenv_path=".env")
    api_key = os.getenv("OPENAI_API_KEY")
    return api_key