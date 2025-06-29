from flask import request, jsonify, g
from app.blueprints.v1.kpi import kpis_bp
from app.models import KPI, Insight
from app.blueprints.v1.kpi.schemas import kpi_schema, kpis_schema
from app.extension import db
from app.blueprints.v1.upload.routes import ask_openai
from app.utils.utils import token_required


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
@token_required
def get_kpi():
    # Get the department from the logged-in user
    user_department = g.current_user.department

    # Filter KPIs to only those from user's department
    department_kpis = KPI.query.filter_by(department=user_department).all()

    return jsonify(kpis_schema.dump(department_kpis)), 200

@kpis_bp.route('/<int:kpi_id>/insight', methods=['GET'])
def get_kpi_insight(kpi_id):
    kpi = KPI.query.get(kpi_id)

    if not kpi:
        return jsonify({'error': f'KPI with ID {kpi_id} not found'}), 404

    try:
        # Build the AI prompt
        question = (
            f"This KPI is '{kpi.kpi_name}' with an actual value of {kpi.value} {kpi.unit or ''}. "
            f"The target goal is {kpi.target_goal} over a {kpi.target_window or 'N/A'} window. "
            f"What could be the root cause of this KPI performance?"
        )

        # Call OpenAI
        insight_text = ask_openai(question)

        # Save to database
        new_insight = Insight(
            kpi_id=kpi.kpi_id,
            insight_text=insight_text
        )
        db.session.add(new_insight)
        db.session.commit()

        return jsonify({
            'kpi_id': kpi.kpi_id,
            'kpi_name': kpi.kpi_name,
            'insight': insight_text
        }), 200

    except Exception as e:
        return jsonify({'error': f'Failed to generate or save insight: {str(e)}'}), 500