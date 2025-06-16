from app.models import KPI
from app.extension import ma

class KPISchema(ma.SQLAlchemySchema):
    class Meta:
        model = KPI
        load_instance = True

    kpi_id = ma.auto_field()
    upload_id = ma.auto_field()
    kpi_name = ma.auto_field()
    value = ma.auto_field()
    unit = ma.auto_field()
    target_goal = ma.auto_field()
    target_window = ma.auto_field()

kpi_schema = KPISchema()
kpis_schema = KPISchema(many=True)