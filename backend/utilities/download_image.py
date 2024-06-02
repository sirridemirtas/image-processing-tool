from flask import request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os


def download_image():
    from server import app

    filename = request.args.get('filename')
    if not filename:
        return jsonify({'error': 'Filename is required'})

    filename = secure_filename(filename)

    folder_path = app.config['FOLDER_PROCESSED_IMAGES']
    if not os.path.exists(folder_path):
        return jsonify({'error': 'Folder not found', 'folder': folder_path})

    file_path = os.path.join(folder_path, filename)
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found', 'file': file_path})

    return send_from_directory(app.config['FOLDER_PROCESSED_IMAGES'], filename)
