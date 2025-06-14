from app.blueprints import KPI
from app.extension import ma

class KPISchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = KPI

kpi_schema = KPISchema()
kpis_schema = KPISchema(many=True)