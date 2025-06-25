from functools import wraps
from flask import request, jsonify, g

# Example hardcoded users and tokens
EMPLOYEE_TOKENS = {
    "Bearer manager-token-123": {
        "employee_id": "E001",
        "role": "manager",
        "department": "ICU"
    },
    "Bearer director-token-456": {
        "employee_id": "E002",
        "role": "director",
        "department": "All"
    }
}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        
        if not token or token not in EMPLOYEE_TOKENS:
            return jsonify({"message": "Unauthorized"}), 401

        # Store user context for use in route
        g.current_user = EMPLOYEE_TOKENS[token]
        return f(*args, **kwargs)
    
    return decorated
