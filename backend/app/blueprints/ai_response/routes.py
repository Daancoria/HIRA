from flask import Blueprint, request, jsonify

# Define the blueprint
ai_response_bp = Blueprint('ai_response', __name__)

# Define the /analyze route
@ai_response_bp.route('/analyze', methods=['POST'])
def analyze():
    prompt = request.json.get('prompt', '')
    
    # Echo back the prompt
    return jsonify({
        "reply": f"✅ Backend received: {prompt}"
    })
