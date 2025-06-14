from . import db

class Upload(db.Model):
    __tablename__ = 'Uploads'

    upload_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
    file_name = db.Column(db.String(100), nullable=False)
    file_type = db.Column(db.String(50))
    upload_time = db.Column(db.DateTime, server_default=db.func.now())

    # relationships
    kpis = db.relationship('KPI', backref='upload', lazy=True)
    staffing_data = db.relationship('StaffingData', backref='upload', lazy=True)
