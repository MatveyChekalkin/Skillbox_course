import os

# C: Users Cheka PycharmProjects python-ds 23_Files 05_save
def save_file(text):
    path_put = input('Куда хотите сохранить документ? '
                 'Введите последовательность папок (через пробел):\n').replace(' ', '/')
    file_name = input('Введите имя файла: ') + '.txt'
    path = path_put + '/' + file_name
    if os.path.exists(path_put):
        if file_name in os.listdir(path_put):
            answer = input('\nВы действительно хотите перезаписать файл? ').lower()
            if answer == 'да':
                file = open(path, 'w', encoding='utf-8')
                file.write(text)
                file.close()
                print('Файл перезаписан')
            elif answer == 'нет':
                print(f'Файл {file_name} уже существует')
                save_file(text)
            else:
                print('Ошибка ввода ')
                save_file(text)
        elif file_name not in os.listdir(path_put):
            file = open(path, 'w', encoding='utf-8')
            file.write(text)
            file.close()
            print('Файл записан')
    else:
        print('\nНе верный путь, попробуйте еще разок')
        save_file(text)


save_file(input('Введите строку: '))