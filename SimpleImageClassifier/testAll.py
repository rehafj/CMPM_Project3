import os
import pprint

from test import *

pp = pprint.PrettyPrinter(indent=4)

directroy = "dataset/test/"

results = {}

for foldername in os.listdir(directroy):
    if os.path.isdir(directroy+foldername):
        results[foldername] = {}
        for filename in os.listdir(directroy+foldername):
            print("starting %s"%filename)
            try:
                if foldername == test(directroy+foldername+"/"+filename):

                    if foldername in results[foldername]:
                        results[foldername][foldername] += 1
                    else:
                        results[foldername][foldername] = 1
            except:
                continue

pp.pprint(results)
