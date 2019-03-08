import glob
import os

f_in = open("./attacks/test.txt", "r")
f_out = open("./attacks/attacks.json", "a")

f_out.write("[\n")
for line in f_in:
    f_out.write("\t{\n")
    f_out.write("\t\t\"type\": \"" + line.split(',', 1)[0] + "\",\n")
    f_out.write("\t\t\"description\": " + line.split(',', 1)[1])
    f_out.write("\t},\n")
f_out.write("]\n")
