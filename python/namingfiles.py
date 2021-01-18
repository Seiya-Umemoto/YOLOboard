from glob import glob
import os
import re

files = glob("/home/seiya/yoloboard/can_data/valid_images/*.jpg")

files = sorted(files, key=lambda file: int(re.findall("[0-9]+", file)[0]))

with open('/home/seiya/yoloboard/can_data/can_validating.txt', 'w') as f:
    for file in files:
        f.write("%s\n" % file)