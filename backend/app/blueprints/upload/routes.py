import os
import fitz  # for PDF reading
import openai # for GPT-3.5
from flask import request, jsonify
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from app.blueprints.upload import uploads_bp

# --- Load environment variables ---
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# --- Config ---
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'csv', 'docx'}

# --- Helpers ---
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_file_contents(filepath):
    file_ext = filepath.rsplit('.', 1)[1].lower()
    try:
        if file_ext == 'txt':
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()

        elif file_ext == 'pdf':
            text = ''
            doc = fitz.open(filepath)
            for page in doc:
                text += page.get_text()
            return text

        else:
            return "Unsupported file type."

    except Exception as e:
        return f"Error reading file: {str(e)}"

def ask_openai(question, context=None):
    try:
        messages = [{"role": "user", "content": question}]
        if context:
            messages.insert(0, {"role": "system", "content": f"Context:\n{context}"})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Error: {str(e)}"


# --- Routes ---
@uploads_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part in request'}), 400

    file = request.files['file']
    question = request.form.get('question', '')  # Optional user question

    if file.filename == '':
        return jsonify({'message': 'No file selected'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        file.save(filepath)

        # Extract content and ask OpenAI
        context = extract_file_contents(filepath)
        bot_response = ask_openai(question, context=context)

        return jsonify({
            'message': 'File uploaded and processed successfully',
            'filename': filename,
            'bot_response': bot_response
        }), 200

    return jsonify({'message': 'Invalid file type'}), 400
