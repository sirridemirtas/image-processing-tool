import os
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename

from config import Config
from utilities import upload_image
from actions import brightness, contrast, flip, gaussian_blur, grayscale, rgb_order, rotate, scale

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
# Example: http://localhost:5000/process?filename=sample.jpg&rotate=23&flip=1&brightness=50
# Supported actions: look at config.py
@ app.route('/process', methods=['GET'])
def process_image():
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

    # file not exist in processed folder
    processed_folder_path = app.config['FOLDER_PROCESSED_IMAGES']
    if not os.path.exists(processed_folder_path):
        os.makedirs(processed_folder_path)

    # copy file to processed folder
    processed_file_path = os.path.join(
        processed_folder_path, filename)
    os.system(f'cp {file_path} {processed_file_path}')

    actions = {action: request.args.get(action)
               for action in app.config['SUPPORTED_ACTIONS']}

    image_path = os.path.join(app.config['FOLDER_RAW_IMAGES'], filename)

    # return actions
    for action, value in actions.items():
        if value:
            if action == 'brightness':
                #  value: 0 to 100
                image_path = brightness(image_path, int(value))
            elif action == 'contrast':
                #  value: 0 to 100
                image_path = contrast(image_path, int(value))
            elif action == 'flip':
                #  value: 0 - Vertical, 1 - Horizontal
                image_path = flip(image_path, int(value))
            elif action == 'gaussian_blur':
                #  value: kernel size: 3, 5, 7, 9, 11 ...
                image_path = gaussian_blur(image_path, int(value))
            elif action == 'grayscale':
                #  value: 0 - Red, 1 - Green, 2 - Blue
                image_path = grayscale(image_path, int(value))
            elif action == 'rgb_order':
                #  value: RGB, BGR, BRG, GBR, GRB, RBG
                image_path = rgb_order(image_path, value)
            elif action == 'rotate':
                #  value: angle in degrees
                image_path = rotate(image_path, int(value))
            elif scale == 'scale':
                #  value: scale factor: 0.1, 0.5, 1, 2, 5 ...
                image_path = scale(image_path, float(value))

    return send_from_directory(app.config['FOLDER_PROCESSED_IMAGES'], os.path.basename(image_path))


if __name__ == '__main__':
    app.run(debug=True)
