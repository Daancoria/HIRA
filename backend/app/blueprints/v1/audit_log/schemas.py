from app.blueprints.v1 import AuditLog
from app.extension import ma

class AuditLogSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AuditLog

auditlog_schema = AuditLogSchema()
auditlogs_schema = AuditLogSchema(many=True)