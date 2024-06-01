
import cv2


def scale(image_path, value=1):
    '''
    image: OpenCV image
    value: 0 to 100
    return: image_path
    '''
    image = cv2.imread(image_path)
    image = cv2.resize(image, (0, 0), fx=value, fy=value)

    scale_image_path = image_path.replace(
        'raw', 'processed')
    cv2.imwrite(scale_image_path, image)

    return scale_image_path
