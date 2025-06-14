from app.blueprints import AIResponse
from app.extension import ma

class AIResponseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AIResponse

airesponse_schema = AIResponseSchema()
airesponses_schema = AIResponseSchema(many=True)