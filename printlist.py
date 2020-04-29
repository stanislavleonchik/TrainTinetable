def print_list(list_books):
    for el in list_books:
        print('автор: %-5s, цена: %5.2f количество: %4d ' % (el['author'], el['price'], el['count']))
    print()