import os.path
import string
import sys

EXT = '.txt'  
SPLIT_COUNT = 3


def get_file_from_dir(looking_dir: str, ext: str) -> list:
    
    files = []
    for file in os.listdir(looking_dir):
        if file.lower().endswith(ext):
            files.append(os.path.join(looking_dir, file))
    return files


def load_file_content(fn: str) -> list:
   
    if not os.path.isfile(fn):
        return None

    content = None
    try:
        with open(fn, 'r', encoding='utf-8') as file:
            content = file.read()
    except:
        pass

    if not content:
        try:
            with open(fn, 'r') as file:
                content = file.read()
        except:
            pass
    if not content:
        return None

    return content.splitlines()


def input_start_param():
   
    looking_dir = str(input('Введите папку, где искать файлы: '))
    if not looking_dir:
        print('Не задана папка!')
        sys.exit()
    if not os.path.isdir(looking_dir):
        print(f'Не найдена указанная папка "{looking_dir}"!')
        sys.exit()
    searching_word = str(input('Введите слово, которое будем искать: '))
    if not searching_word:
        print('Не задано слово!')
        sys.exit()

    return looking_dir, searching_word


def get_before_indexes(split_str: list, searching_word: str) -> tuple:
   
    end_ind = split_str.index(searching_word)
    start_ind = end_ind - SPLIT_COUNT
    if start_ind < 0:
        start_ind = 0
    return start_ind, end_ind


def get_after_indexes(split_str: list, searching_word: str) -> tuple:
   
    start_ind = split_str.index(searching_word) + 1
    end_ind = start_ind + SPLIT_COUNT
    if end_ind > len(split_str) - 1:
        end_ind = len(split_str)

    return start_ind, end_ind


def build_str(indexes: tuple, split_str: list) -> str:
    tmp_list = []
    for i in range(indexes[0], indexes[1]):
        tmp_list.append(split_str[i])
    ready_str = ' '.join(tmp_list)
    return ready_str


def check_one_file_content(content: list, searching_word: str):
    
    if not content:
        print('Пустое содержимое!')
        return None
    founded = 0
    for txt_str in content:
        split_str = txt_str.translate(str.maketrans(dict.fromkeys(string.punctuation))).split()
        if searching_word not in split_str:
            continue
        founded += 1

        before_str = build_str(get_before_indexes(split_str, searching_word), split_str)
        after_str = build_str(get_after_indexes(split_str, searching_word), split_str)
        ready_str = f'{before_str} ***{searching_word}*** {after_str}'
        print(ready_str)
    print(f'Количество найденных слов = {founded}')


def main():
  
    looking_dir, searching_word = input_start_param()

    all_files = get_file_from_dir(looking_dir, EXT)
    if not all_files:
        print(f'Не удалось найти ни одного файла с расширением "{EXT}"')
        sys.exit()

    for fn_num, fn in enumerate(all_files):
        print(f'{"="*10}> Обрабатывается файл "{fn}" [{fn_num+1}/{len(all_files)}]')
        content = load_file_content(fn)
        if not content:
            print('Не удалось получить содержимое файла!')
            continue
        check_one_file_content(content, searching_word)


if __name__ == '__main__':
    main()
