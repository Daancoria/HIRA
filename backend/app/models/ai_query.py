from . import db

class AIQuery(db.Model):
    __tablename__ = 'ai_queries'

    query_id = db.Column(db.Integer, primary_key=True)
    convo_id = db.Column(db.Integer, db.ForeignKey('ai_conversations.convo_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    kpi_id = db.Column(db.Integer, db.ForeignKey('KPI.kpi_id'))
    query_text = db.Column(db.String(1000))
    time_stamp_date = db.Column(db.DateTime, server_default=db.func.now())

    ai_response = db.relationship('AIResponse', backref='query', lazy=True, uselist=False)
