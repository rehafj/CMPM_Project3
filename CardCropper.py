import glob
import os

from PIL import Image

image_list = []
for filename in glob.glob('cards/*.png'):
    im = Image.open(filename)
    im = im.crop((30, 40, 220, 170))
    im.save(filename)
