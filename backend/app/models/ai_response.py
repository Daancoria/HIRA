from . import db

class AIResponse(db.Model):
    __tablename__ = 'ai_responses'

    response_id = db.Column(db.Integer, primary_key=True)
    query_id = db.Column(db.Integer, db.ForeignKey('ai_queries.query_id'))
    response_text = db.Column(db.String(500))
    confidence_score = db.Column(db.Integer)
    time_stamp_date = db.Column(db.DateTime, server_default=db.func.now())
