from glob import glob
import os
import re

files = glob("/home/seiya/yoloboard/glinder_data/valid_images/*.jpg")

try:
    files = sorted(files, key=lambda file: int(re.findall("[0-9]+", file)[-1]))
except IndexError:
    print("check the names of the images")

with open('/home/seiya/yoloboard/glinder_data/glinder_valid.txt', 'w+') as f:
    for file in files:
        f.write(f"{file}{os.linesep}")