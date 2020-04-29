from stdafx import *
def extractfile(filename):
    while True:
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                return pickle.load(file)
        else:
            print('Файл с таким названием отсутствует')
            return