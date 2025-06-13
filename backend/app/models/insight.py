from . import db

class Insight(db.Model):
    __tablename__ = 'Insight'

    insight_id = db.Column(db.Integer, primary_key=True)
    kpi_id = db.Column(db.Integer, db.ForeignKey('KPI.kpi_id'), nullable=False)
    root_cause = db.Column(db.String(500))
    recommendation = db.Column(db.String(500))
    confidence_score = db.Column(db.Numeric(5, 2))
