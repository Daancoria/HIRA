from app.blueprints.v1 import AIQuery
from app.extension import ma


class AIQuerySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AIQuery

aiquery_schema = AIQuerySchema()
aiqueries_schema = AIQuerySchema(many=True)
