from . import db

class KPI(db.Model):
    __tablename__ = 'KPI'

    kpi_id = db.Column(db.Integer, primary_key=True)
    upload_id = db.Column(db.Integer, db.ForeignKey('Uploads.upload_id'), nullable=False)
    kpi_name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Numeric(12, 4))
    unit = db.Column(db.String(50))
    target_goal = db.Column(db.Numeric(12, 4))
    target_window = db.Column(db.String(50))

    # relationship to insights
    insights = db.relationship('Insight', backref='kpi', lazy=True)
    ai_queries = db.relationship('AIQuery', backref='kpi', lazy=True)
