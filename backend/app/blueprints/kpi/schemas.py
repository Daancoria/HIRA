from app.models import KPI
from app.extension import ma

class KPISchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = KPI
        load_instance = True

kpi_schema = KPISchema()
kpis_schema = KPISchema(many=True)