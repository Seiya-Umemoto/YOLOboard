import subprocess
import os

os.chdir('..')

process = subprocess.Popen(['./darknet','detector','test','can_data/can.data','cfg/yolov4-custom.cfg',
        'can_data/backup/yolov4-custom_best.weights','can_data/test_images/20210115_201403.bag'],
        stdout=subprocess.PIPE,
        universal_newlines=True)

with open("python/test_log.txt", "w+") as f:
    while True:
        output = process.stdout.readline()
        f.write(output)
        print(output.rstrip())
        return_code = process.poll()
        if return_code is not None:
            lines = process.stdout.readlines()
            for output in lines:
                f.write(output)
                print(output.rstrip())
            break