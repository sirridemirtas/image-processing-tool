from flask import request, jsonify
from werkzeug.utils import secure_filename
import os
import uuid
from server import app


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file and allowed_file(file.filename):
        if file.filename is not None:
            filename, file_extension = os.path.splitext(file.filename)
        else:
            return jsonify({'error': 'Invalid file name'})

        # Generate a unique filename using UUID and keep the original extension
        unique_filename = str(uuid.uuid4()) + file_extension
        filename = secure_filename(unique_filename)
        file_path = os.path.join(app.config['FOLDER_RAW_IMAGES'], filename)
        file.save(file_path)
        return jsonify({
            'filename': filename,
            'url': f'http://localhost:5000/static/uploads/{filename}',
        })
    return jsonify({'error': 'File type not allowed'})
