name = input('Название файла: ')
sym = [i for i in '@№$%^&*()']
if name[0] not in sym \
        and (name.endswith('.txt')
             or name.endswith('.docx')):
    print('Файл назван верно.')
elif name[0] in sym:
    print('Ошибка: название начинается на один из специальных символов')
else:
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
