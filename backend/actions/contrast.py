from PIL import Image, ImageEnhance


def contrast(image_path, value):
    '''
    value: 0 - 100
    return: image_path
    '''
    image = Image.open(image_path)
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(value / 50.0)

    contrast_image_path = image_path.replace(
        'raw', 'processed')
    image.save(contrast_image_path)

    return contrast_image_path
