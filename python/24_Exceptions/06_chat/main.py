import os
# Не очень ясно, что нужно сделать

def choice():
    try:
        print(f'Выбирете действие:\n'
              '1) Посмотреть текущий текст чата\n'
              '2) Отправить сообщение (затем вводит сообщение) Действия запрашиваются бесконечно.')
        num = int(input('Ваш выбор: '))
        if 1 < num > 2:
            raise SyntaxError
    except SyntaxError:
        choice()
    else:
        return num

def one(name_id, id):
    with open(os.path.abspath('chat.txt'), 'r', encoding='utf-8') as file:
        for i in file:
            print(i)
    try:
        answer = int(input('1 - Написать\n'
                           '2-выйти\n'))
        if answer == 1:
            two(name_id, id)
    except:
        one(name_id, id)

def two(name_id, id):
    with open(os.path.abspath('chat.txt'), 'a', encoding='utf-8') as file:
        file.write(f'{name_id[id]} написал: {input("Введите сообщение: ")}\n')

name_id = {1: 'Алиса', 2: 'Макс', 3: 'Оля'}

while True:
    try:
        id = int(input('Введите id: '))
        if id not in name_id.keys():
            raise SystemError
        else:
             res = choice()
             if res == 1:
                 fst = one(name_id, id)
             elif res == 2:
                 twt = two(name_id, id)
    except SystemError:
        print('Отсутствует id')
    except ValueError:
        print('введите коректно id')
