import whatimage
import pyheif
from PIL import Image
import os
import io
import sys
import subprocess
from os import listdir
from os.path import isfile, join

# def decodeImage(bytesIo):
#     with open(bytesIo,'rb') as f:
#         data = f.read()
#     fmt = whatimage.identify_image(data)
#     if fmt in map(lambda x:x.lower(),['HEIC', 'avif']):
#         i = pyheif.read_heif(data)
        
#         for metadata in i.metadata or []:
#             if metadata['type'] == 'Exif':
#                 pass
        
#         s = io.BytesIO()
#         pi = Image.frombytes(
#             mode=i.mode, size=i.size, data=i.data
#         )
#         pi.save(s, format="jpeg")

# decodeImage("/home/seiya/yoloboard/can_data2/train_images/IMG_0228.HEIC")

if len(sys.argv) != 2:
    print('usage python c.py path_to_directory_containing_images')
else:
    mypath = sys.argv[1]
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    outdir = os.path.join(mypath, 'train_images')
    # if not os.path.exits(outdir):
    #     os.makedirs(outdir)
    # else:
    #     print("Output dir already exits.")
    #     exit(0)
    for file in onlyfiles:
        (name, ext) = os.path.basename(file).split('.')
        
        if ext.lower() == 'heic':
            dest = os.path.join(outdir, name) + '.jpg'
            source = os.path.join(mypath, file)