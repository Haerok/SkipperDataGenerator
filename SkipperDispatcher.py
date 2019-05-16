import os
import os.path
import shutil
from SkipperDataGenerator import *


def is_video(extension):
    if extension == '.mpg' or extension == '.mxf' or extension \
        == '.mp4' or extension == '.ts':
        return True
    else:
        return False


def is_cablelabs(extension):
    if extension == '.xml':
        return True
    else:
        return False


def watcher():
    while True:
        list_of_file = os.listdir(RECEPTION_dir_path)
        for file in list_of_file:
            filename = os.path.splitext(file)
            if is_video(filename[1]):
                for side_file in list_of_file:
                    side_file_name = os.path.splitext(side_file)
                    if filename[0] == side_file_name[0] \
                        and is_cablelabs(side_file_name[1]):
                        shutil.move(RECEPTION_dir_path + '/'
                                    + filename[0] + filename[1],
                                    WORK_dir_path + '/' + filename[0]
                                    + filename[1])
                        data_generator(WORK_dir_path + '/'
                                + filename[0] + filename[1])
    return 0


watcher()

			
