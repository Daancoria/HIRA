import os
import pandas as pd
from flask import request, jsonify
from werkzeug.utils import secure_filename
from app.blueprints.staffing_data import staffing_data_bp
from app.models import StaffingData
from app.extension import db

ALLOWED_EXTENSIONS = {'csv'}
UPLOAD_FOLDER = 'uploads'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@staffing_data_bp.route('/upload-staffing', methods=['POST'])
def upload_staffing_data():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        file.save(filepath)

        try:
            df = pd.read_csv(filepath)
            records = df.to_dict(orient='records')

            for row in records:
                staffing = StaffingData(
                    pay_period=row.get('Pay Period'),
                    facility=row.get('Facility'),
                    cost_center=row.get('Cost Center'),
                    functional_grouping=row.get('Functional Grouping'),
                    unit_type=row.get('Unit Type'),
                    department=row.get('Department'),
                    statistic=row.get('Statistic'),
                    target_hours_per_statistic=row.get('Target Hours per Statistic'),
                    productive_hours=row.get('Productive Hours'),
                    actual_statistic=row.get('Actual Statistic'),
                    hours_earned=row.get('Hours Earned'),
                    hours_per_uos=row.get('Hours per UOS'),
                    actual_productive_ftes=row.get('Actual Productive FTEs'),
                    flex_productive_ftes=row.get('Flex Productive FTEs'),
                    flex_actual_percentage=row.get('Flex /Actual Percentage'),
                    actual_vs_flex_ftes_variance=row.get('Actual v Flex Productive FTE Variance'),
                    actual_nonproductive_ftes=row.get('Actual Non-Productive FTEs'),
                    budget_nonproductive_ftes=row.get('Budget Non-Productive FTEs'),
                    actual_vs_budget_nonproductive_ftes_variance=row.get('Actual v Bud Non-Productive FTE Variance'),
                    actual_total_ftes=row.get('Actual Total FTEs'),
                    premium_pay_percentage=row.get('Premium Pay Percentage'),
                    total_salaries=row.get('Total Salaries'),
                    budget_cost_per_uos=row.get('Budget Cost per UoS'),
                    actual_cost_per_uos=row.get('Actual Cost per UoS'),
                    variance=row.get('variance')
                )
                db.session.add(staffing)

            db.session.commit()
            return jsonify({'message': 'Staffing data uploaded successfully'}), 201

        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500

    return jsonify({'error': 'Invalid file type'}), 400
