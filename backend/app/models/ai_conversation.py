from . import db

class AIConversation(db.Model):
    __tablename__ = 'ai_conversations'

    convo_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    started_at = db.Column(db.DateTime, server_default=db.func.now())

    ai_queries = db.relationship('AIQuery', backref='conversation', lazy=True)
