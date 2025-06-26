import os
import fitz
import openai
import pandas as pd
from app.blueprints.upload import uploads_bp
from flask import request, jsonify, current_app
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from app.models import Upload, KPI, DatasetRow
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
        return f"Error: {str(e)}"

@uploads_bp.route('/', methods=['POST'])
def upload_and_store_dataset():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    user_id = int(request.form.get('user_id', 1))  # fallback for now
    question = request.form.get('question')

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    filename = secure_filename(file.filename)
    file_ext = filename.rsplit('.', 1)[1].lower()
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

    os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)
    file.save(filepath)

    # Save upload metadata
    new_upload = Upload(
        user_id=user_id,
        file_name=filename,
        file_type=file_ext
    )
    db.session.add(new_upload)
    db.session.commit()

    response = {
        'message': 'File uploaded and saved successfully',
        'upload_id': new_upload.upload_id,
        'filename': filename
    }

    errors = []
    inserted = 0

    try:
        df = pd.read_csv(filepath)
        df = df.dropna(how='all')  # drop empty rows

        for row_index, row in df.iterrows():
            for key, value in row.items():
                key_str = str(key).strip()
                value_str = str(value).strip() if pd.notna(value) else None

                # Skip if key is empty or value is NaN/null
                if not key_str or value_str is None:
                    continue

                dataset_row = DatasetRow(
                    upload_id=new_upload.upload_id,
                    hospital_id="H001",
                    row_index=row_index,
                    key=key_str,
                    value=value_str
                )
                db.session.add(dataset_row)
                inserted += 1

        db.session.commit()

        # Optional: analyze with OpenAI
        if question:
            summary = df.head(10).to_string()
            answer = ask_openai(question, context=summary)
            response['bot_response'] = answer

        response['rows_inserted'] = inserted
        return jsonify(response), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to process CSV: {str(e)}'}), 500



@uploads_bp.route('/<int:upload_id>/rows', methods=['GET'])
def get_uploaded_rows(upload_id):
    try:
        rows = DatasetRow.query.filter_by(upload_id=upload_id).all()

        if not rows:
            return jsonify({'message': 'No data found for this upload'}), 404

        return jsonify({
            'upload_id': upload_id,
            'total_rows': len(rows),
            'data': [
                        {
                            'hospital_id': row.hospital_id,
                            'row_index': row.row_index,
                            'key': row.key,
                            'value': row.value
                        } for row in rows
                    ]
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    


    