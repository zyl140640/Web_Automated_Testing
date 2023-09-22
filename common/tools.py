import os
import random
from os import listdir

import ffmpy


def detect_video():
    my_path = "./case_video/"

    for file_name in listdir(my_path):

        if file_name.endswith('.webm'):
            os.remove(my_path + file_name)


# 需要转换格式的视频文件，文件真实存在


if __name__ == '__main__':
    source_file = r"./case_video/690aef8da37bcef1a286f4db627324b0.webm"
    # 转换成功后的视频文件，文件夹真实存在，不会自动创建
    sum = random.randint(1, 100)
    sink_file = f"./case_video/{sum}.mp4"

    ff = ffmpy.FFmpeg(
        inputs={source_file: None},
        outputs={sink_file: None})
    print(ff)
    ff.run()

