# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

# Import models after db object created
from app.models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize db
    db.init_app(app)

    # Test route to verify connection
    @app.route("/")
    def index():
        return "HIRA Backend Connected!"

    return app

