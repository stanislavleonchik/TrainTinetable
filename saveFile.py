from stdafx import *
def save_file(data):
    with open(input('Сохранить как: ').strip() + '.pkl', 'wb') as file:
        pickle.dump(data, file)
