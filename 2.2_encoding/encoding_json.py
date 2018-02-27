from operator import itemgetter
from get_file_path import PWD
import os
import json
import chardet

print('Введите номер файла для анализа.\nДоступные файлы:\n')
available_files = list(os.listdir(path='%s/json_files' % PWD))
dict_input = {}
for i in range(len(available_files)):
    dict_input[i + 1] = available_files[i]

for key, value in dict_input.items():
    print('{}: {}'.format(key, value))

print()
current_file = int(input())


def load_file():
    with open('%s/json_files/%s' % (PWD, dict_input[current_file]), 'rb') as f:
        data = f.read()
        result = chardet.detect(data)
        text = data.decode(result['encoding'])
        text = json.loads(text)
        return text


def top_words(text):
    length_filter = int(input('\nВведите минимальную длину слова.\n'))
    word_amount = int(input('Введите количество слов в топе.\n'))

    word_list = []  #формируем список слов
    i = 0
    for data in text['rss']['channel']['items']:
        for key, value in data.items():
            if key not in ['description', 'title']: continue
            word_list.append(value.split())

    word_list_filtered = []  #в этом списке будут слова, проходящие фильтр длины
    for data in word_list:
        for word in data:
            if len(word) <= length_filter: continue
            word_list_filtered.append(word.strip().lower())
    
    del word_list   #удаляем ставший ненужным список

    word_set = set(word_list_filtered)  #убираем дубли из списка слов
    word_count = {}  #создаем словарь для хранения пар слов "слово: количество упоминаний"
    for word in word_set:
        word_count[word] = word_list_filtered.count(word)

    #если запрос пользователя превышает количесто отфильтрованных слов, то вывести все возможные
    word_count_len = len(word_count.values())
    if word_amount > word_count_len: word_amount = word_count_len

    word_count = sorted(word_count.items(), key=itemgetter(1), reverse=True)

    print('\nТоп-{} слов в тексте:'.format(word_amount))

    i = 0
    for pair in word_count:
        print('{}: {}'.format(pair[0], pair[1]))
        i += 1
        if i == word_amount: break


top_words(load_file())

