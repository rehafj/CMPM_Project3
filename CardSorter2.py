import os
import glob
import shutil
import random

for filename in glob.glob('Water/*.png'):
    print(filename)
    name_ext = filename.split("\\")[1]
    # print(name_ext)
    name = name_ext.split(".")[0]
    name_dir = "Water/" + name_ext
    rand = random.randint(1, 100)
    if (rand > 80):
        shutil.move(name_dir, "./Test/Water/" + name_ext)
    elif (rand > 16):
        shutil.move(name_dir, "./Train/Water/" + name_ext)
    else:
        shutil.move(name_dir, "./Val/Water/" + name_ext)
