from glob import glob                                                           
import cv2 
import os
#change to *.jpeg to conver jpeg to jpg
imgs = glob('/home/seiya/yoloboard/glinder_data/valid_images/*.bmp')

for img in imgs:
    print(img)
    new_img = cv2.imread(img)
    # change -3 to -4 to covert extension of size 4
    cv2.imwrite(img[:-3] + 'jpg', new_img)
    os.remove(img)