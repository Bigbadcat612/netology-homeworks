import subprocess
import sys
import os
from multiprocessing import Pool

if len(sys.argv) <= 1 or sys.argv[1].lower() == '-help':
    print(
        '\n\nПрограмма принимает аргументы в следующем виде: "[папка с изображениями], [ширина отредактированного изображения], [папка для сохранения изображений]". Без запятых и кавычек.\n\nПример запуска программы: python C:\programs\external_progs.py C:\images 300 C:\images_edited.\n\nПредварительно создавать папки не обязательно.\nРаботает на всех OS.'
    )
    sys.exit(0)

INPUT_FOLDER = sys.argv[1]
RESIZE = sys.argv[2]
OUTPUT_FOLDER = sys.argv[3]

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)


def make_file_list(folder):
    file_list = os.listdir(folder)
    return file_list


def resize_and_save_image(file):
    path_input = os.path.join(INPUT_FOLDER, file)
    path_output = os.path.join(OUTPUT_FOLDER, file)
    process = subprocess.Popen(
        'convert {} -resize {} {}'.format(path_input, RESIZE, path_output),
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    log = {
        'errors': process.stderr.read(),
        'output_message': process.stdout.read()
    }

    return log


file_list = make_file_list(INPUT_FOLDER)

if __name__ == '__main__':
    pool = Pool(4)
    pool.map(resize_and_save_image, file_list)

    pool.close()
    pool.join()
