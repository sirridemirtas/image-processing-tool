from PIL import Image


def grayscale(image_path, band='r'):
    '''
    Convert image to grayscale
    band: 0 - Red, 1 - Green, 2 - Blue
    '''

    image = Image.open(image_path)
    image = image.convert('RGB')

    if band == 'r':
        image = image.convert('L')
    elif band == 'g':
        r, g, b = image.split()
        image = g
    elif band == 'b':
        r, g, b = image.split()
        image = b

    grayscale_image_path = image_path.replace(
        'raw', 'processed')
    image.save(grayscale_image_path)

    return grayscale_image_path
