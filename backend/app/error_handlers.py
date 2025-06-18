import logging
from flask import Blueprint, jsonify
from werkzeug.exceptions import HTTPException

# Create a blueprint for error handling 
error_bp = Blueprint('error_bp', __name__)

# Set up a logger for this module
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # You can change to INFO or WARNING for production or we can create another logger for production

# Function to register error handlers with the Flask app
def register_error_handlers(app):

    # Handle all HTTP exceptions (e.g., 404 Not Found, 401 Unauthorized)
    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        # Log warnings or errors for specific status codes
        if error.code >= 500:
            logger.error(f"HTTPException {error.code}: {error.name} - {error.description}")
        elif error.code == 404:
            logger.warning(f"404 Not Found: {error.description}")
        else:
            logger.info(f"Handled HTTP exception: {error}")

        return jsonify({
            "error": error.name,
            "message": error.description,
            "code": error.code
        }), error.code

    # Handle generic unhandled exceptions (system failures, programming bugs)
    @app.errorhandler(Exception)
    def handle_generic_exception(e):
        # This will catch things like RuntimeError, ValueError, etc.
        logger.critical("Unhandled exception occurred", exc_info=True)

        response = {
            "error": "Internal Server Error",
            "description": str(e),
            "code": 500
        }
        return jsonify(response), 500
