from PIL import Image


def open_image(path):
    return Image.open(path, mode='r')


def save_image(image, path, save_format='jpeg'):
    image.save(path, save_format)


def get_pixel(image, i, j):
    if i > image.width or j > image.height:
        return None

    else:
        pixel = image.getpixel((i, j))
        return pixel


def create_image(i, j):
    image = Image.new("RGB", (i, j), 'white')
    return image
