from PIL import Image


def rgb_order(image_path, order='rgb'):
    '''
    order: rgb, gbr, brg, bgr, grb, rbg 
    '''
    image = Image.open(image_path)
    r, g, b = image.split()
    if order == 'rgb':
        image = Image.merge('RGB', (r, g, b))
    elif order == 'gbr':
        image = Image.merge('RGB', (g, b, r))
    elif order == 'brg':
        image = Image.merge('RGB', (b, r, g))
    elif order == 'bgr':
        image = Image.merge('RGB', (b, g, r))
    elif order == 'grb':
        image = Image.merge('RGB', (g, r, b))
    elif order == 'rbg':
        image = Image.merge('RGB', (r, b, g))
    else:
        image = Image.merge('RGB', (r, g, b))

    rgb_image_path = image_path.replace(
        'raw', 'processed')
    image.save(rgb_image_path)

    return rgb_image_path
