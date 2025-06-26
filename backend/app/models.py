from . import db

class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    # department = db.Column(db.String(100), nullable=False)


    # relationships (optional)
    uploads = db.relationship('Upload', backref='user', lazy=True)
    audit_logs = db.relationship('AuditLog', backref='user', lazy=True)
    ai_conversations = db.relationship('AIConversation', backref='user', lazy=True)
    ai_queries = db.relationship('AIQuery', backref='user', lazy=True)


class Upload(db.Model):
    __tablename__ = 'Uploads'

    upload_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    file_name = db.Column(db.String(100), nullable=False)
    file_type = db.Column(db.String(50))
    upload_time = db.Column(db.DateTime, server_default=db.func.now())

    # relationships
    kpis = db.relationship('KPI', backref='upload', lazy=True)
    staffing_data = db.relationship('StaffingData', backref='upload', lazy=True)
    
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

class KPI(db.Model):
    __tablename__ = 'KPI'

    kpi_id = db.Column(db.Integer, primary_key=True)
    upload_id = db.Column(db.Integer, db.ForeignKey('Uploads.upload_id'), nullable=False)
    kpi_name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Numeric(12, 4))
    unit = db.Column(db.String(50))
    target_goal = db.Column(db.Numeric(12, 4))
    target_window = db.Column(db.String(50))
    department = db.Column(db.String(100), nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'department': self.department,
            'metric': self.metric,
            'value': self.value,
        }

    # relationship to insights
    insights = db.relationship('Insight', backref='kpi', lazy=True)
    ai_queries = db.relationship('AIQuery', backref='kpi', lazy=True)
    
class Insight(db.Model):
    __tablename__ = 'Insight'

    insight_id = db.Column(db.Integer, primary_key=True)
    kpi_id = db.Column(db.Integer, db.ForeignKey('KPI.kpi_id'), nullable=False)
    root_cause = db.Column(db.String(500))
    recommendation = db.Column(db.String(500))
    confidence_score = db.Column(db.Numeric(5, 2))
    
class AuditLog(db.Model):
    __tablename__ = 'Audit_Logs'

    audit_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    action = db.Column(db.String(350))
    audit_timestamp = db.Column(db.DateTime, server_default=db.func.now())
    
class AIResponse(db.Model):
    __tablename__ = 'ai_responses'

    response_id = db.Column(db.Integer, primary_key=True)
    query_id = db.Column(db.Integer, db.ForeignKey('ai_queries.query_id'))
    response_text = db.Column(db.String(500))
    confidence_score = db.Column(db.Integer)
    time_stamp_date = db.Column(db.DateTime, server_default=db.func.now())
    
class AIQuery(db.Model):
    __tablename__ = 'ai_queries'

    query_id = db.Column(db.Integer, primary_key=True)
    convo_id = db.Column(db.Integer, db.ForeignKey('ai_conversations.convo_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    kpi_id = db.Column(db.Integer, db.ForeignKey('KPI.kpi_id'))
    query_text = db.Column(db.String(1000))
    time_stamp_date = db.Column(db.DateTime, server_default=db.func.now())

    ai_response = db.relationship('AIResponse', backref='query', lazy=True, uselist=False)
    
class AIConversation(db.Model):
    __tablename__ = 'ai_conversations'

    convo_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    started_at = db.Column(db.DateTime, server_default=db.func.now())

    ai_queries = db.relationship('AIQuery', backref='conversation', lazy=True)
    
class DatasetRow(db.Model):
    __tablename__ = 'dataset_rows'

    id = db.Column(db.Integer, primary_key=True)
    hospital_id = db.Column(db.String(100), nullable=True)  # If known
    upload_id = db.Column(db.Integer, db.ForeignKey('data_input.id'), nullable=True)
    row_index = db.Column(db.Integer, nullable=True)  # Original row number in the CSV
    key = db.Column(db.String(255), nullable=False)   # Column name (can be blank or unknown)
    value = db.Column(db.Text, nullable=True)         # Store all data as-is, no cleanup

    __table_args__ = (
        db.Index('ix_datasetrow_hospital_key', 'hospital_id', 'key'),
    )
    upload_id = db.Column(db.Integer, db.ForeignKey('Uploads.upload_id'), nullable=True)
    upload = db.relationship('Upload', backref='dataset_rows')
