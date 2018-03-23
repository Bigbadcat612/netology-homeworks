import requests
import json
import sys
import os
import chardet

KEY = 'trnsl.1.1.20180321T131932Z.9a3531442a0c6022.49ce7059a8eb154301a2f03edfe3a1cd4c484d17'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

if len(sys.argv) <= 1 or sys.argv[1] == '-help':
    print('Программа принимает аргументы в следующем виде: "[путь к исходному файлу] [путь, куда сохранить файл] [направление перевода, например it-fr или ru-en]"\n\nПример запуска программы: python C:/programs/requests_python.py C:/Documents/input.txt C:/Documents/output.txt ru-en\n\nРаботает на всех системах.')
    sys.exit(0)

INPUT_FILE = sys.argv[1]
OUTPUT_FILE = sys.argv[2]
LANG = sys.argv[3]


if not os.path.exists(os.path.dirname(OUTPUT_FILE)):
    os.makedirs(os.path.dirname(OUTPUT_FILE))


def make_file_unicoded(file):
    #Функция считывает файл и кодирует текст в юникоде
    print('Подготавливаю файл...')
    with open(file, 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        text = data.decode(result['encoding'])
        text = text.encode('utf-8', 'ignore')
        text = text.decode('utf-8')
        return text


def get_translate(text):
    print('Перевожу текст...')
    params = dict(
    key = KEY,
    text = text,
    lang = LANG,
    format = 'plain',
    options = 1
    )

    response = requests.get(URL, params)
    response = json.loads(response.text)

    translated_text = response['text'][0]

    return translated_text


def write_result(text):
    with open(OUTPUT_FILE, 'w', encoding='UTF-8') as f:
        f.write(text)
    return 'Done'


translated_file = get_translate(make_file_unicoded(INPUT_FILE))
write_result(translated_file)
print('Готово!')