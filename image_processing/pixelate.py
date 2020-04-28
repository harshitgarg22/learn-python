from PIL import Image
from utils_pixelate import create_image, get_pixel


def pixelate(image, STEP=50):

    width, height = image.size

    outImage = create_image(width, height)
    pixels = outImage.load()

    for i in range(0, width, STEP):
        for j in range(0, height, STEP):

            for a in range(0, STEP):
                for b in range(0, STEP):
                    try:
                        pixels[i + a, j + b] = get_pixel(image, i, j)
                    except:
                        pass

    # Return new image
    return outImage
