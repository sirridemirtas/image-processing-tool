import os


class Config:
    # Construct absolute paths
    FOLDER_RAW_IMAGES = os.path.join(os.getcwd(), 'static', 'images', 'raw')
    FOLDER_PROCESSED_IMAGES = os.path.join(
        os.getcwd(), 'static', 'images', 'processed')

    SUPPORTED_ACTIONS = [
        'blur',
        'brightness',
        'contrast',
        'flip',
        'gaussian_blur',
        'grayscale',
        'rgb_order',
        'rotate',
    ]

    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
