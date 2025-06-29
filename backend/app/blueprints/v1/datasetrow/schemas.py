from app.models import DatasetRow
from app.extension import ma

class DatasetRowSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = DatasetRow

dataset_schema = DatasetRowSchema()
datasets_schema = DatasetRowSchema(many=True)