from app.blueprints.v1.ai_conversation import AIConversation
from app.extension import ma

class AIConversationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = AIConversation

aiconversation_schema = AIConversationSchema()
aiconversations_schema = AIConversationSchema(many=True)