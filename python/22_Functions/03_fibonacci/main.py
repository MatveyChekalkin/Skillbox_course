def num_pos(num):
    if num <= 2:
        return 1
    n1 = num_pos(num -1)
    n2 = num_pos(num -2)
    return n1+n2

num = int(input('Введите позицию числа в ряде Фибоначчи: '))
print(f'Число: {num_pos(num)}')

# def num_pos(num):
#     f = [i for i in range(1, num + 1)]
#     for i, n in enumerate(f):
#         if i < 2:
#             f[i] = 1
#         else:
#             f[i] = f[i - 1] + f[i - 2]
#     return f[num-1]
#
#
# num = int(input('Введите позицию числа в ряде Фибоначчи: '))
# print(f'Число: {num_pos(num)}')
