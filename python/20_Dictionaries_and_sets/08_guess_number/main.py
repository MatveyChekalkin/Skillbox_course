# Задание не очень!!!я понимаю, что на множества, но какая логика не понятно!!!
# Все работает но на рандоме т. к не понятен алгоритм логики того который отгадывает

import random as r

maxnum = int(input('Введите максимальное число: '))
num = set(range(1, maxnum + 1))

while True:
    prob = set(range(1, r.randint(3, maxnum) + 1, r.randint(1, 3)))
    print(f'Нужное число есть среди вот этих чисел: {prob}')
    answer = input('Ответ Артёма:').lower()
    if answer == 'да':
        num = num.intersection(prob)
    elif answer == 'нет':
        num = num.difference(prob)
    elif answer == 'помогите!':
        print(f'Артём мог загадать следующие числа: {num}')
        break
