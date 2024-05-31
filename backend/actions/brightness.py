import cv2
import numpy as np


def brightness(image_path, value):
    '''
    value: Parlaklık değeri, 0 ile 100 arasında bir tam sayı olmalıdır.
    '''

    # Parlaklık değerinin sınırları kontrol edilir
    if not (0 <= value <= 100):
        raise ValueError("Brightness value must be between 0 and 100")

    # Resmi oku
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image at {image_path} could not be found")

    # Parlaklık değerini artırmak için matris oluştur
    brightness_matrix = np.ones(image.shape, dtype="uint8") * value

    # Parlaklık artırılmış resmi elde et
    bright_image = cv2.add(image, brightness_matrix)

    # Parlaklığı artırılmış resmi kaydet
    bright_image_path = image_path.replace('raw', 'processed')
    cv2.imwrite(bright_image_path, bright_image)

    return bright_image_path
