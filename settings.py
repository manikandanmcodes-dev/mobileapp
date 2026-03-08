import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent

# AI model
LLM_MODEL = "llama-3.3-70b-versatile"

# Groq API key from .env
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Vector database path
CHROMA_DB_PATH = BASE_DIR / "database" / "chroma"