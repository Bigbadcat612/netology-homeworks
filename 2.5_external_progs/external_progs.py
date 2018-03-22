"""
АЛГОРИТМ

Программа принимает следующие sys.argv: файл/папка для обработки, команду что нужно сделать, папку для аутпута
1. Программа проверяет, указал пользователь путь к папке или к одному изображению

"""

import subprocess
import sys
import os

if sys.argv[1].lower() == '-help':
    print('Программа принимает аргументы в следующем виде: "папка с изображениями, ширина изображения, папка для сохранения изображений". Без запятых и кавычек.')
    sys.exit(0)
INPUT_FOLDER = sys.argv[1]
RESIZE = sys.argv[2]
OUTPUT_FOLDER = sys.argv[3]

if not os.path.exists(OUTPUT_FOLDER):
    os.mkdir(OUTPUT_FOLDER)

def make_file_list(folder):
    file_list = os.listdir(folder)
    return file_list
    
def resize_and_save_images(file_list):
    for image in file_list:
        subprocess.run('convert {}\{} -resize {} {}\{}'.format(INPUT_FOLDER, image, RESIZE, OUTPUT_FOLDER, image))
    
resize_and_save_images(make_file_list(INPUT_FOLDER))