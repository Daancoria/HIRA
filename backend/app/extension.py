from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import firebase_admin
from firebase_admin import credentials, auth
import os
from dotenv import load_dotenv



db = SQLAlchemy()
ma = Marshmallow()
cache = Cache()
limiter = Limiter(key_func=get_remote_address)

load_dotenv()
cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")

print("Firebase credentials path:", cred_path)

if cred_path and not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)