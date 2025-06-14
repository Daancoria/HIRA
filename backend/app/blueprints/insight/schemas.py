from app.blueprints import Insight
from app.extension import ma

class InsightSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Insight

insight_schema = InsightSchema()
insights_schema = InsightSchema(many=True)