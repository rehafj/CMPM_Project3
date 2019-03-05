import glob
import os

from PIL import Image

image_list = []
for filename in glob.glob('cards/*.png'): 
    im=Image.open(filename)
    im = im.crop((30, 40, 200, 170))
    im.save(filename + '_c.png')
