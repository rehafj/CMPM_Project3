###
### Takes a list of pokemon names in CSV format 
### and converts them to JSON (for text classifier validation)
###

import glob
import os

f_in = open("names.txt", "r")
f_out = open("names-json.txt", "a")

f_out.write("[\n")
for line in f_in:
    f_out.write("\t{\n")
    f_out.write("\t\t\"type\": \"" + line.split(',', 1)[0] + "\",\n")
    f_out.write("\t\t\"name\": " + "\"" + line.split(',', 1)[1].replace('\n', "").replace(" ", "") + "\"\n")
    f_out.write("\t},\n")
f_out.write("]\n")
