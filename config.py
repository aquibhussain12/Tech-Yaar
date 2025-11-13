import os
from dotenv import load_dotenv

load_dotenv()

# Gemini API key (get it from https://aistudio.google.com/app/apikey)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# SQLite database URI
DB_PATH = "sqlite:///techyaar.db"
