from app.models import User
from app.extension import ma
from marshmallow import Schema, fields, validate

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True
        load_instance = True

    name = fields.Str(required=True)  # Now required
    email = fields.Email(required=True)
    password = fields.String(required=True)
    role = fields.String(
        required=True,
        validate=validate.OneOf(["Manager", "Director"])
    )

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class LoginSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    role = fields.Str(required=True)

login_schema = LoginSchema()
