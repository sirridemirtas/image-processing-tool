import cv2


def gaussian_blur(image_path, kernel_size=5):
    '''
    image: OpenCV image
    kernel_size: odd number 3, 5, 7, 9, 11
    return: image_path
    '''
    if kernel_size % 2 == 0:
        kernel_size += 1

    image = cv2.imread(image_path)
    image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    blur_image_path = image_path.replace(
        'raw', 'processed')
    cv2.imwrite(blur_image_path, image)

    return blur_image_path
