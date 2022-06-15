import random
import os

# with open(os.path.abspath('coordinates.txt'), 'a', encoding='utf-8') as coordinates:
#     for i in range(0,int(input('Введите колво пар: '))):
#         print(f'Введите {i + 1} пару чисел через пробел:', end=' ')
#         nums = input().split()
#         coordinates.write(f'{nums[0]} {nums[1]}\n')

def f(x, y):
    try:
        x += random.randint(0, 10)
        y += random.randint(0, 5)
        res_1 = x / y
    except ZeroDivisionError:
        print('В первой функции значение y = 0, на ноль делить нельзя (Функция вернула 0)')
        return 0
    else:
        return res_1


def f2(x, y):
    try:
        x -= random.randint(0, 10)
        y -= random.randint(0, 5)
        res_2 = y / x
    except ZeroDivisionError:
        print('В второй функции значение x = 0, на ноль делить нельзя (Функция вернула 0)')
        return 0
    else:
        return res_2


with open(os.path.abspath('coordinates.txt'), 'r', encoding='utf-8') as file:
    for i, line in enumerate(file):
        nums_list = line.split()
        try:
            res_1 = f(int(nums_list[0]), int(nums_list[1]))
            res_2 = f2(int(nums_list[0]), int(nums_list[1]))
            number = random.randint(0, 100)
            with open(os.path.abspath('result.txt'), 'a', encoding='utf-8') as file_2:
                my_list = sorted([res_1, res_2, number])
                file_2.write(' '.join((str(my_list[0]),str(my_list[1]),str(my_list[2]))) + '\n')
        except ValueError:
            print(f'В файле coordinates.txt в {i + 1} строке значение '
                  f'{nums_list[0]} или {nums_list[1]} введено неправильно')