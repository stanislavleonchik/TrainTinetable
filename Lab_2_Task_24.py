import input_time_table
import saveFile
from extractfile import extractfile
from printlist import print_list


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
        LB.append(input_time_table.input_time(len(LB)))
    elif p == '2':
        # Печать:
        print_list(LB)
    elif p == '3':
        # Сортировка по автору:
        LB.sort(key=(lambda x: x['author']))
    elif p == '4':
        saveFile.save_file(LB)
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
