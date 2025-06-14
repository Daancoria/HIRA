from . import db

class User(db.Model):
    __tablename__ = 'Users'

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(100), nullable=False)

    # relationships (optional)
    uploads = db.relationship('Upload', backref='user', lazy=True)
    audit_logs = db.relationship('AuditLog', backref='user', lazy=True)
    ai_conversations = db.relationship('AIConversation', backref='user', lazy=True)
    ai_queries = db.relationship('AIQuery', backref='user', lazy=True)
