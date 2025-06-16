import os
import fitz
import openai
import pandas as pd
from app.blueprints.upload import uploads_bp
from flask import request, jsonify, current_app
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from app.models import Upload, KPI
from app.extension import db


# --- Load API Key ---
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# --- Config ---
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'csv', 'docx'}

# --- Helpers ---
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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
            return "Unsupported file type for text extraction."
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

# --- File Upload Route ---
@uploads_bp.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part in request'}), 400

    file = request.files['file']
    question = request.form.get('question')
    user_id = int(request.form.get('user_id', 1))

    if file.filename == '':
        return jsonify({'message': 'No file selected'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_ext = filename.rsplit('.', 1)[1].lower()
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)
        file.save(filepath)

        # Optional: Extract context and ask OpenAI only if a question is given
        context = None
        bot_response = None
        if question:
            context = extract_file_contents(filepath)
            bot_response = ask_openai(question, context)

        # Save file metadata to Uploads table
        new_upload = Upload(
            user_id=user_id,
            file_name=filename,
            file_type=file_ext
        )
        db.session.add(new_upload)
        db.session.commit()

        response = {
            'message': 'File uploaded and saved to database successfully',
            'filename': filename,
            'file_type': file_ext,
            'upload_id': new_upload.upload_id
        }

        if bot_response:
            response['bot_response'] = bot_response

        return jsonify(response), 200

    return jsonify({'message': 'Invalid file type'}), 400

# --- KPI CSV Ingest Route ---
@uploads_bp.route('/csv-ingest', methods=['POST'])
def ingest_kpi_csv():
    if 'file' not in request.files:
        return jsonify({'error': 'CSV file not found in request'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not file or not allowed_file(file.filename) or not file.filename.endswith('.csv'):
        return jsonify({'error': 'Invalid file type — must be .csv'}), 400

    try:
        df = pd.read_csv(file)

        # Validate required columns
        required_columns = {'upload_id', 'kpi_name', 'value', 'unit', 'target_goal', 'target_window'}
        missing = required_columns - set(df.columns)
        if missing:
            return jsonify({'error': f'Missing columns: {missing}'}), 400

        inserted = 0
        errors = []

        for _, row in df.iterrows():
            try:
                kpi = KPI(
                    upload_id=int(row['upload_id']),
                    kpi_name=row['kpi_name'],
                    value=float(row['value']),
                    unit=row['unit'],
                    target_goal=float(row['target_goal']),
                    target_window=row['target_window']
                )
                db.session.add(kpi)
                inserted += 1
            except Exception as e:
                errors.append(f"Row {row.to_dict()} - {str(e)}")

        db.session.commit()

        stats = df[['value', 'target_goal']].describe().to_dict()

        return jsonify({
            'message': f'{inserted} KPI records inserted successfully.',
            'errors': errors,
            'stats': stats
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
