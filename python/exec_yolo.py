from datetime import datetime, timedelta
import subprocess
import os

start = datetime.now()
start_date_time = start.strftime("%Y-%m-%d_%H:%M:%S")

os.chdir('..')

# 평균 이미지 데이터 크기 (한 장 당 몇 KB...)

process = subprocess.Popen(['./darknet','detector','test','can_data3/can.data',
        'cfg/yolov4-custom.cfg','yolov4.conv.137','-dont_show','-map'],
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

    end = datetime.now()
    end_date_time = end.strftime("%Y-%m-%d_%H:%M:%S")

    duration = end - start
    duration = duration - timedelta(microseconds=duration.microseconds)

    result = "start: " + start_date_time + ", " + "end: " + end_date_time + ", " + "duration: " + str(duration)
    print(result)
    f.write(result)
