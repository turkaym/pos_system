"""
Application configuration.

Loads environment variables from .env file.
"""

from dotenv import load_dotenv
from pathlib import Path
import os

# Project root (pos system)
BASE_DIR = env_path = Path(os.getcwd()) / ".env"

# Load .env file
load_dotenv(dotenv_path=env_path)
