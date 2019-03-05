import glob
import os

from PIL import Image

image_list = []
for filename in glob.glob('cards/*.png'): #assuming gif
    # print(filename)
    im=Image.open(filename)
    im = im.crop((1, 1, 98, 33))
    im.save(filename + '_cropped.png')

    #image_list.append(im)


        # try:
        #
        #     im = Image.open(f).convert('L')
        #     im = im.crop((1, 1, 98, 33))
        #     im.save('_0.png')
        # except (KeyboardInterrupt, SystemExit):
        #     raise
        # except Exception as e:
        #     print("Ignoring problem file:", f)
        #     print(str(e))
        #     print(repr(e))
        #     continue
