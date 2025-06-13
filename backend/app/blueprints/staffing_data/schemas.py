from app.blueprints import StaffingData
from app.extension import ma

class Staffing_DataSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = StaffingData

staffing_data_schema = Staffing_DataSchema()
staffing_data_schema = Staffing_DataSchema(many=True)