qwt_num = int(input('Кол-во чисел: '))
num_list = []
for _ in range(qwt_num):
    num = int(input('Число: '))
    num_list.append(num)

if num_list == num_list[::-1]:
    print(f'\nПоследовательность чисел: {num_list} симетрична')
else:
    count = 0
    for i in range(len(num_list) - 1, 0 - 1, -1):
        if num_list[i] != num_list[i - 1]:
            num_list.append(num_list[i-1])
            count += 1

print('Последовательность:', num_list[0:len(num_list) - count])
print('Нужно приписать чисел:', count)
print('Сами числа:', num_list[-count:])
