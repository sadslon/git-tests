import re


def clear_names(file_name: str) -> list:
    ''' Функция очистки имен от лишних символов'''

    new_names_list = list()

    with open('../data/' + file_name, encoding='utf-8') as names_file:
        names_list = names_file.read().split()
        for name_item in names_list:
            new_name = ''
            for symbol in name_item:
                if symbol.isalpha():
                    new_name += symbol
            if new_name:
                new_names_list.append(new_name)

    return new_names_list

def is_cyrillic(name_item: str) -> bool:
    ''' Проверка на вхождение кириллицы в строку'''
    return bool(re.search('[а-яА-Я]', name_item))


def russian_names_list(names_list: list) -> list:
    ''' Имена написанные на русском языке'''
    new_names_list = list()
    for name_item in names_list:
        if is_cyrillic(name_item):
            new_names_list.append(name_item)
    return new_names_list


if __name__ == '__main__':
    cleared_name = clear_names('names.txt')

    print(russian_names_list(cleared_name))
