from flask import request
from app.models import AuditLog, SecurityLog, DataChangeLog
from app.extension import db

def log_audit(user_id, action):
    log = AuditLog(
        user_id=user_id,
        action=action,
        ip_address=request.remote_addr,
        endpoint=request.path,
        method=request.method,
        user_agent=request.headers.get('User-Agent')
    )
    db.session.add(log)
    db.session.commit()

def log_security(event_type, description):
    log = SecurityLog(
        event_type=event_type,
        description=description,
        ip_address=request.remote_addr,
        user_agent=request.headers.get('User-Agent')
    )
    db.session.add(log)
    db.session.commit()

def log_data_change(table_name, row_id, action, old_data, new_data, user_id=None):
    log = DataChangeLog(
        table_name=table_name,
        row_id=row_id,
        action=action,
        old_data=old_data,
        new_data=new_data,
        changed_by=user_id
    )
    db.session.add(log)
    db.session.commit()
