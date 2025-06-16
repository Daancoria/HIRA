# app/routes/kpi_routes.py
from flask import request, jsonify
from app.blueprints.kpi import kpis_bp
from app.models import KPI
from app.blueprints.kpi.schemas import kpi_schema, kpis_schema
from app.extension import db


@kpis_bp.route('/', methods=['POST'])
def create_kpi():
    data = request.get_json()
    try:
        new_kpi = KPI(
            upload_id=data['upload_id'],
            kpi_name=data['kpi_name'],
            value=data.get('value'),
            unit=data.get('unit'),
            target_goal=data.get('target_goal'),
            target_window=data.get('target_window')
        )
        db.session.add(new_kpi)
        db.session.commit()
        return kpi_schema.jsonify(new_kpi), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@kpis_bp.route('/', methods=['GET'])
def get_kpis():
    all_kpis = KPI.query.all()
    return kpis_schema.jsonify(all_kpis)
