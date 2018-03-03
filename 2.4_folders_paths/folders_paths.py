import os

pwd = os.path.dirname(os.path.abspath(__file__))


def choose_folder():
    folders_dict = {}
    folders_list = list(filter(os.path.isdir, os.listdir(pwd)))
    print('Введите номер папки из доступных:')

    for i in range(len(folders_list)):
        folders_dict[i + 1] = folders_list[i]

    for key, value in folders_dict.items():
        print('{}: {}'.format(key, value))

    user_input = int(input())

    return folders_dict[user_input]


current_folder = choose_folder()


def choose_files(folder):
    print('Введите формат искомого файла без точки. Например "sql"')
    format_filter = '.' + str(input()).lower()
    working_files = os.listdir('{}/{}'.format(pwd, folder))
    working_files = list(filter(lambda x: format_filter in x, working_files))
    if working_files == []: return print('Ничего не найдено.')

    return working_files


def iterative_find(working_files):
    if working_files == None: return
    print('Учитывать регистр при поиске? Да/нет')
    register = str(input()).lower()

    print('Искать слово целиком или учитывать все совпадения? Да/нет')
    whole_phrase = str(input()).lower()

    while True:
        print('Введите фрагмент для поиска:')
        user_input = str(input())
        del_indices = []
        for i in range(len(working_files)):
            with open('{}/{}/{}'.format(pwd, current_folder, working_files[i]), 'r') as f:
                txt = f.read()
                if register == 'нет':
                    txt = txt.lower()
                    user_input = user_input.lower()

                if whole_phrase == 'да':
                    cleaned_txt = []
                    for word in txt.split():
                        cleaned_txt.append(word.strip('.,!-*:;…?«»'))
                    txt = cleaned_txt

                if user_input not in txt: del_indices.append(i)

        for i in sorted(del_indices, reverse=True):
            del working_files[i]

        print('\nНайдено:\n')
        print('\n'.join(working_files))
        print('Всего файлов: {}'.format(len(working_files)))

    return


print(iterative_find(choose_files(current_folder)))

