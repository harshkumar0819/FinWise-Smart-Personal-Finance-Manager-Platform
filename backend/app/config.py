
import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")

class Config:
    _secret_key = os.environ.get("SECRET_KEY")

    if not _secret_key or not _secret_key.strip():
        raise ValueError("SECRET_KEY is missing or empty. Please check your .env file.")

    SECRET_KEY = _secret_key.strip()

    DEBUG = os.environ.get("FLASK_ENV") == "development"

    _mongo_uri = os.environ.get("MONGODB_URI")

    if not _mongo_uri or not _mongo_uri.strip():
        raise ValueError("MONGODB_URI is missing or empty. Please check your .env file.")

    MONGODB_URI = _mongo_uri.strip()

    DB_NAME = os.environ.get("DB_NAME", "finwise_db").strip()
