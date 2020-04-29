def input_time(bookindex):
    dict_book = {}
    print('Книга %d: ' % (bookindex + 1))
    dict_book['author'] = input('Автор книги: ')
    dict_book['price'] = float(input('Цена: '))
    dict_book['count'] = int(input('Количество: '))
    return dict_book
