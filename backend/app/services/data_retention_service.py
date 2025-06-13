from datetime import datetime, timedelta
from app.models import db, Upload, KPI, Insight, StaffingData, AIConversation, AIQuery, AIResponse, AuditLog

class DataRetentionService:

    @staticmethod
    def cleanup_expired_data():
        now = datetime.utcnow()

        # Uploads (1 year retention)
        upload_cutoff = now - timedelta(days=365)
        expired_uploads = Upload.query.filter(Upload.upload_time < upload_cutoff).all()
        for upload in expired_uploads:
            # Cascade delete: KPIs, Staffing Data handled via relationships if properly set (we’ll configure later)
            db.session.delete(upload)

        # AI Conversations (6 month retention)
        convo_cutoff = now - timedelta(days=180)
        expired_convos = AIConversation.query.filter(AIConversation.started_at < convo_cutoff).all()
        for convo in expired_convos:
            db.session.delete(convo)

        # Audit Logs (7 year retention)
        audit_cutoff = now - timedelta(days=365 * 7)
        expired_audits = AuditLog.query.filter(AuditLog.audit_timestamp < audit_cutoff).all()
        for audit in expired_audits:
            db.session.delete(audit)

        db.session.commit()
        print("Data retention cleanup complete.")

