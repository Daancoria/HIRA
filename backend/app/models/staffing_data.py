from . import db

class StaffingData(db.Model):
    __tablename__ = 'Staffing_Data'

    id = db.Column(db.Integer, primary_key=True)
    upload_id = db.Column(db.Integer, db.ForeignKey('Uploads.upload_id'), nullable=False)

    pay_period = db.Column(db.String(50))
    facility = db.Column(db.String(50))
    cost_center = db.Column(db.String(50))
    functional_grouping = db.Column(db.String(100))
    unit_type = db.Column(db.String(100))
    department = db.Column(db.String(100))
    statistic = db.Column(db.String(100))

    target_hours_per_statistic = db.Column(db.Numeric(12, 4))
    productive_hours = db.Column(db.Numeric(12, 4))
    actual_statistic = db.Column(db.Numeric(12, 4))
    hours_earned = db.Column(db.Numeric(12, 4))
    hours_per_uos = db.Column(db.Numeric(12, 4))
    actual_productive_ftes = db.Column(db.Numeric(12, 4))
    flex_productive_ftes = db.Column(db.Numeric(12, 4))
    flex_actual_percentage = db.Column(db.Numeric(12, 4))
    actual_v_flex_productive_fte_variance = db.Column(db.Numeric(12, 4))
    actual_non_productive_ftes = db.Column(db.Numeric(12, 4))
    budget_non_productive_ftes = db.Column(db.Numeric(12, 4))
    actual_v_budget_non_productive_fte_variance = db.Column(db.Numeric(12, 4))
    actual_total_ftes = db.Column(db.Numeric(12, 4))
    premium_pay_percentage = db.Column(db.Numeric(5, 2))
    total_salaries = db.Column(db.Numeric(14, 2))
    budget_cost_per_uos = db.Column(db.Numeric(14, 2))
    actual_cost_per_uos = db.Column(db.Numeric(14, 2))
    variance = db.Column(db.Numeric(14, 2))
