# Takes a list of card images in a directory and crops them down to
# just the image of the pokemon

import glob
import os

from PIL import Image

for filename in glob.glob('cards/*.png'):
    im = Image.open(filename)
    im = im.crop((30, 40, 220, 150))
    im.save(filename)
