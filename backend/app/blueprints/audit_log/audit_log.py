from . import db

class AuditLog(db.Model):
    __tablename__ = 'Audit_Logs'

    audit_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
    action = db.Column(db.String(350))
    audit_timestamp = db.Column(db.DateTime, server_default=db.func.now())
