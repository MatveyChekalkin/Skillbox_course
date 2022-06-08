number = int(input('Введите число N: '))
number_list = []

for n in range(1, number + 1):
    if n % 2 != 0:
        number_list.append(n)
print('Список нечетных чисел от 1 до', number, '\n', number_list)