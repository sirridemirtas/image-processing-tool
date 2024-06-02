import cv2


def flip(image_path, flip_code):
    '''
    flip_code: h: x ekseninde simetri, v: y ekseninde simetri, b: hem x hem y ekseninde simetri
    '''

    flip_code = 1 if flip_code == 'h' else 0 if flip_code == 'v' else -1

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
