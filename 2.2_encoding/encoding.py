import chardet
from operator import itemgetter
from get_file_path import PWD
import os

print('Выберите файл для анализа.\nДоступные файлы:')
available_files = list(os.listdir(path='%s/sourcefiles' % PWD))
for file in available_files:
    print(file)

print()
current_file = str(input())


def top_words():
    with open('%s/sourcefiles/%s' % (PWD, current_file), 'rb') as f:
        length_filter = int(input('\nВведите минимальную длину слова.\n'))
        word_amount = int(input('Введите количество слов в топе.\n'))

        data = f.read()
        result = chardet.detect(data)
        text = data.decode(result['encoding'])

        word_list = text.split()  #формируем список слов
        word_list_filtered = []  #в этот список будем добавлять которые соответствуют фильтру длины слова
        for i in range(len(word_list)):
            if len(word_list[i]) <= length_filter: continue
            word_list_filtered.append(word_list[i].strip().lower())  #убираем лишние пробелы и приводим слова к нижнему регистру

        del word_list  #теперь старый список можно удалить (вопрос: а надо ли?)

        word_set = set(word_list_filtered)  #убираем дубли из списка слов
        word_count = {}                     #создаем словарь для хранения пар слов "слово: количество упоминаний"
        for word in word_set:
            word_count[word] = word_list_filtered.count(word)

        word_count_len = len(word_count.values())
        if word_amount > word_count_len:  #если запрос пользователя превышает количесто отфильтрованных слов, то вывести все возможные
            word_amount = word_count_len

        word_count = sorted(
            word_count.items(), key=itemgetter(1), reverse=True)

        print('\nТоп-{} слов в тексте:'.format(word_amount))

        i = 0
        for pair in word_count:
            print('{}: {}'.format(pair[0], pair[1]))
            i += 1
            if i == word_amount: break


top_words()

