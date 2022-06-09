# import random as r
#
# num_list = [r.randint(0, 10) for x in range(int(input('Сколько чисел? ')))]

num_list = [int(input('Введите число: ')) for x in range(int(input('Сколько чисел? ')))]

print(f'\nпервоначальный список {num_list}')
for _ in range(num_list.count(0)):
    num_list.append(num_list.pop(num_list.index(0)))

print(f'\n0 перенесены в конец массива: {num_list}')
num_list[-num_list.count(0):] = []
print(f'\nСжатый список {num_list}')