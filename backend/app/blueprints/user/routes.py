from app.blueprints.user import users_bp
from app.blueprints.user.schemas import user_schema, users_schema, login_schema
from app.models import User, db
from flask import request, jsonify
from marshmallow import ValidationError
from sqlalchemy import select, delete
from app.utils.utils import encode_token

    
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



@users_bp.route("/login", methods=["POST"])
def login():
    try:
        credentials = login_schema.load(request.json)
        name = credentials['name']
        email = credentials['email']
        password = credentials['password']
        role = credentials['role']
    except ValidationError as e:
        return jsonify(e.messages), 400

    query = select(User).where(
        User.email == email,
        User.role == role
    )
    customer = db.session.execute(query).scalars().first()

    if customer and customer.password == password:
        token = encode_token(customer.id)
        response = {
            'status': 'success',
            'message': 'successfully logged in',
            'token': token
        }
        return jsonify(response), 200
    else:
        return jsonify({"message": "Invalid login credentials"}), 400
    
@users_bp.route("/", methods=["GET"])
def get_all_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users)), 200