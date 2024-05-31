import cv2


def flip(image_path, flip_code):
    '''
    flip_code: 0: x ekseninde simetri, 1: y ekseninde simetri, -1: hem x hem y ekseninde simetri
    '''

    # Resmi oku
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image at {image_path} could not be found")

    # Resmi döndür
    flipped_image = cv2.flip(image, flip_code)

    # Döndürülmüş resmi kaydet
    flipped_image_path = image_path.replace('raw', 'processed')
    cv2.imwrite(flipped_image_path, flipped_image)

    return flipped_image_path
