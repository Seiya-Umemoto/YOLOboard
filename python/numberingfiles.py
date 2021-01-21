from glob import glob                                                           
import cv2 
import os
import re

files = glob('/home/seiya/yoloboard/can_data2/test_images/*.jpg')

dirname = os.path.dirname(files[0])

files = sorted(files, key=lambda file: int(re.findall("[0-9]+", file)[1]))

print(dirname)

num = 1
for file in files:
    print(file, num)
    os.rename('{0}'.format(file),'{0}/{1}.jpg'.format(dirname, num))
    num += 1