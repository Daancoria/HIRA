from app.blueprints.v1.user import users_bp
from app.blueprints.v1.user.schemas import user_schema, users_schema, login_schema
from app.models import User, db
from flask import request, jsonify
from marshmallow import ValidationError
from sqlalchemy import select, delete
from app.utils.utils import encode_token


import firebase_admin
from firebase_admin import credentials, auth
import os

if not firebase_admin._apps:
    cred = credentials.Certificate(os.getenv("FIREBASE_CREDENTIALS_PATH"))
    firebase_admin.initialize_app(cred)

# ─────────────── ROUTES ─────────────── #

@users_bp.route("/", methods=["POST"])
def create_user():
    try:
        user_data = user_schema.load(request.json)
        print(user_data)
    except ValidationError as e:
        return jsonify(e.messages), 400

    db.session.add(user_data)
    db.session.commit()

    return jsonify(user_schema.dump(user_data)), 201

@users_bp.route("/", methods=["GET"])
def get_all_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users)), 200


@users_bp.route("/login", methods=["POST"])
def firebase_login():
    data = request.get_json()
    firebase_token = data.get("firebase_token")

    if not firebase_token:
        return jsonify({"error": "Missing Firebase token"}), 400

    try:
        decoded_token = auth.verify_id_token(firebase_token)
        email = decoded_token.get("email")
        name = decoded_token.get("name", email.split("@")[0])

        user = User.query.filter_by(email=email).first()

        if not user:
            user = User(
                name=name,
                email=email,
                password="firebase-auth",  # dummy value
                role="Manager"  # or default role
            )
            db.session.add(user)
            db.session.commit()

        jwt_token = encode_token(user.id)

        return jsonify({
            "message": "Login via Firebase successful",
            "user": {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "role": user.role
            },
            "jwt_token": jwt_token
        }), 200

    except Exception as e:
        return jsonify({"error": f"Firebase token invalid: {str(e)}"}), 401
