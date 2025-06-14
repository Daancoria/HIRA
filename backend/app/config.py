# app/config.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable noisy warning logs
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
