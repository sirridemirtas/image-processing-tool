import cv2


def rotate(image_path, angle):
    # Resmi oku
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Image at {image_path} could not be found")

    # Resmin boyutlarını al
    height, width = image.shape[:2]

    # Döndürme merkezini belirle
    center = (width / 2, height / 2)

    # Döndürme matrisini hesapla
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1)

    # Döndürme işlemi sırasında resmin boyutlarını korumak için sinüs ve kosinüs değerlerini hesapla
    abs_cos = abs(rotation_matrix[0, 0])
    abs_sin = abs(rotation_matrix[0, 1])

    # Yeni resmin boyutlarını hesapla
    new_width = int(height * abs_sin + width * abs_cos)
    new_height = int(height * abs_cos + width * abs_sin)

    # Döndürme matrisini ayarla
    rotation_matrix[0, 2] += new_width / 2 - center[0]
    rotation_matrix[1, 2] += new_height / 2 - center[1]

    # Resmi döndür
    rotated_image = cv2.warpAffine(
        image, rotation_matrix, (new_width, new_height))

    # Döndürülmüş resmi kaydet
    rotated_image_path = image_path.replace('raw', 'processed')
    cv2.imwrite(rotated_image_path, rotated_image)

    return rotated_image_path
