from flask_sqlalchemy import SQLAlchemy

# Create db instance (imported in your app/__init__.py)
db = SQLAlchemy()

# Import all models here (so Flask can discover them automatically)
from .user import User
from .upload import Upload
from .kpi import KPI
from .insight import Insight
from .audit_log import AuditLog
from .staffing_data import StaffingData
from .ai_conversation import AIConversation
from .ai_query import AIQuery
from .ai_response import AIResponse
