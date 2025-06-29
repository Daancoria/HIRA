from app.blueprints.v1 import Upload
from app.extension import ma

class UploadSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Upload

upload_schema = UploadSchema()
uploads_schema = UploadSchema(many=True)