from app.error_handlers import register_error_handlers
from flask import Flask
from app.extension import db, ma, limiter, cache
from app.logging_config import setup_logging 
from app.blueprints.user.routes import users_bp
from app.blueprints.upload.routes import uploads_bp
from app.blueprints.kpi.routes import kpis_bp
from app.blueprints.staffing_data.routes import staffing_data_bp
from app.blueprints.ai_response.routes import ai_response_bp  # ✅ NEW

from flask_swagger_ui import get_swaggerui_blueprint as swagger_ui_bp

SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.yaml'

swaggerui_blueprint = swagger_ui_bp(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Your API's Name"
    }
)

def create_app(config_name):
    app = Flask(__name__)
    setup_logging(app)
    app.config.from_object(f'config.{config_name}')
    app.config['UPLOAD_FOLDER'] = 'uploads'
    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024

    db.init_app(app)
    ma.init_app(app)
    limiter.init_app(app)
    cache.init_app(app)

    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(uploads_bp, url_prefix='/uploads')
    app.register_blueprint(kpis_bp, url_prefix='/kpis')
    app.register_blueprint(staffing_data_bp, url_prefix='/staffing_data')
    app.register_blueprint(ai_response_bp)  # ✅ Register the /analyze route here
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    register_error_handlers(app)

    return app
