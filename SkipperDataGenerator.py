import os
import subprocess
import os.path
import ntpath
import shutil
import numpy as np

WORK_dir_path = '/home/labo/Documents/SKIPPER/WORK'
RECEPTION_dir_path = '/home/labo/Documents/SKIPPER/RECEPTION'

def data_generator(video_path):
    video_name = ntpath.basename(video_path)
    video_dir_path = WORK_dir_path + '/' \
        + os.path.splitext(ntpath.basename(video_path))[0] + '_tmp'
    os.mkdir(video_dir_path)
    shutil.move(video_path, video_dir_path + '/' + video_name)
    subprocess.call([
        'ffmpeg',
        '-hide_banner',
        '-ss',
        '0',
        '-t',
        '600',
        '-i',
        video_dir_path + '/' + video_name,
        '-r',
        '25',
        '-s',
        '100x100',
        '-q:v',
        '5',
        '-copyinkf',
        '-y',
        video_dir_path + '/' + os.path.splitext(video_name)[0]
            + '_%08d.bmp',
        ])
    list_of_file = os.listdir(video_dir_path)
    if video_name in list_of_file:
        list_of_file.remove(video_name)

    list_of_file.sort()



			
