from app.blueprints import Upload

class UploadSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Upload

upload_schema = UploadSchema()
uploads_schema = UploadSchema(many=True)