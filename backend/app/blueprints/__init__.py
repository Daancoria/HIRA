from flask_sqlalchemy import SQLAlchemy

# Create db instance (imported in your app/__init__.py)
db = SQLAlchemy()

# Import all models here (so Flask can discover them automatically)
from .user import User
from .upload.upload import Upload
from .kpi.kpi import KPI
from .insight.insight import Insight
from .audit_log.audit_log import AuditLog
from .staffing_data.staffing_data import StaffingData
from .ai_conversation.ai_conversation import AIConversation
from .ai_query.ai_query import AIQuery
from .ai_response.ai_response import AIResponse
