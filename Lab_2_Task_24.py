import pickle
import os


# region 0) Функция печати меню программы:
def menu():
    print(' Меню '.center(46, '='))
    print('| 0) Вывод меню                                        |')
    print('| 1) Добавление элемента в список                      |')
    print('| 2) Вывод списка                                      |')
    print('| 3) Сортировка по автору                              |')
    print('| 4) Сохранение списка словарей в файл                 |')
    print('| 5) Извлечение словарей из файла и запись их в список |')
    print('| 6) Удаление одного элемента из списка                |')
    print('| e) Выход из программы                                |')
    print('=' * 46)


# endregion

# region 1) Добавление элемента в список:
def input_list(bookindex):
    dict_book = {}
    print('Книга %d: ' % (bookindex + 1))
    dict_book['author'] = input('Автор книги: ')
    dict_book['price'] = float(input('Цена: '))
    dict_book['count'] = int(input('Количество: '))
    return dict_book


# endregion

# region 2) Печать списка книг:
def print_list(list_books):
    for el in list_books:
        print('автор: %-5s, цена: %5.2f количество: %4d ' % (el['author'], el['price'], el['count']))
    print()


# endregion

def saveFile(data):
    with open(input('Сохранить как: ').strip() + '.pcl', 'wb') as file:
        pickle.dump(data, file)


def extractfile(filename):
    while True:
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                return pickle.load(file)
        else:
            print('Файл с таким названием отсутствует')
            return


# region ------------------ Основная программа ----------------
LB = []  # - список книг
menu()
tf = True
while tf:
    p = input('Введите номер пункта ')
    if p == '0':
        # Меню:
        menu()
    elif p == '1':
        # Добавление элемента в список:
        LB.append(input_list(len(LB)))
    elif p == '2':
        # Печать:
        print_list(LB)
    elif p == '3':
        # Сортировка по автору:
        LB.sort(key=(lambda x: x['author']))
    elif p == '4':
        saveFile(LB)
    elif p == '5':
        filename = input('Введите название файла: ').strip() + '.pcl'
        LB = extractfile(filename)
    elif p == '6':
        try:
            LB.pop(int(input('Введите номер записи для удаления: ')))
        except IndexError:
            print('Записи с таким номером не существует')
        except ValueError:
            print('Некорректный номер записи')
    elif p in 'eEеЕ':
        tf = False
    else:
        print('Нет такого пункта меню!')
        menu()
# endregion
