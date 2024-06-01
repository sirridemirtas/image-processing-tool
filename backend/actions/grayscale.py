from PIL import Image


def grayscale(image_path, band=0):
    '''
    Convert image to grayscale
    band: 0 - Red, 1 - Green, 2 - Blue
    '''

    image = Image.open(image_path)
    image = image.convert('RGB')

    if band == 0:
        image = image.convert('L')
    elif band == 1:
        r, g, b = image.split()
        image = g
    elif band == 2:
        r, g, b = image.split()
        image = b

    grayscale_image_path = image_path.replace(
        'raw', 'processed')
    image.save(grayscale_image_path)

    return grayscale_image_path
