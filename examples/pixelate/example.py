from pixelate import pixelate
from utils_pixelate import open_image, save_image

import os
import sys

if __name__ == '__main__':
    originalImagePath = os.path.join(
        os.path.realpath(sys.path[0]), 'images', 'original')
    original_file_list = os.scandir(originalImagePath)

    pixelatedImagePath = os.path.join(
        os.path.realpath(sys.path[0]), 'images', 'pixelated')
    pixelated_file_list = os.scandir(pixelatedImagePath)

    num_files = len((next(os.walk(originalImagePath)))[2])
    print('Reading {} files...'.format(num_files))

    steps = {'shapeofwater': 10, 'marriage': 25, 'birdman': 20, 'jaws': 10,
             'dunkirk': 20, 'cmbyn': 20, '127': 20, 'fargo': 20, 'florida': 20, 'moonlight': 25}

    for filename in original_file_list:
        orig = open_image(os.path.join(originalImagePath, filename))

        filmName = os.path.basename(filename.name)
        filmName = ''.join(filmName.split('.')[:-1])

        print('Reading {}...'.format(filmName))
        pixelated = pixelate(orig, steps[filmName])
        save_image(pixelated, os.path.join(pixelatedImagePath, filmName + '.jpg'), 'jpeg')