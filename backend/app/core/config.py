"""
Application configuration.

Loads environment variables from .env file.
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Resolve project root
BASE_DIR = Path(__file__).resolve().parents[3]

ENV_PATH = BASE_DIR / ".env"
load_dotenv(ENV_PATH)

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
