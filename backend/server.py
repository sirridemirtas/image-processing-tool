import os
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename

from config import Config
from utilities import upload_image
from actions import brightness, flip, rotate

app = Flask(__name__)

app.config.from_object(Config)


@app.route('/hello')  # hello world
def hello_world(): return {
    'message': 'Hello World'
}


@app.route('/')  # static folder
def index():
    return app.send_static_file('index.html')


@app.route('/upload', methods=['POST'])
def handele_upload():
    return upload_image()


# Process the uploaded file
# Input: filename, action-value
# Output: Processed image file
# Example: http://localhost:5000/process?filename=sample.jpg&rotate=90&brightness=50
# Supported actions: rotate, flip, grayscale, blur, brightness, contrast
@ app.route('/process', methods=['GET'])
def process_file():
    filename = request.args.get('filename')
    if not filename:
        return jsonify({'error': 'Filename is required'})

    filename = secure_filename(filename)

    folder_path = app.config['FOLDER_RAW_IMAGES']
    if not os.path.exists(folder_path):
        return jsonify({'error': 'Folder not found', 'folder': folder_path})

    file_path = os.path.join(folder_path, filename)
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found', 'file': file_path})

    actions = {action: request.args.get(action)
               for action in app.config['SUPPORTED_ACTIONS']}

    image_path = os.path.join(app.config['FOLDER_RAW_IMAGES'], filename)

    # return actions
    for action, value in actions.items():
        if value:
            if action == 'brightness':
                image_path = brightness(image_path, int(value))
            elif action == 'flip':
                image_path = flip(image_path, int(value))
            elif action == 'rotate':
                image_path = rotate(image_path, int(value))

    return send_from_directory(app.config['FOLDER_PROCESSED_IMAGES'], os.path.basename(image_path))


if __name__ == '__main__':
    app.run(debug=True)
