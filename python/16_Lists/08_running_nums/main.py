n = int(input('Сколько элементов в списке: '))
k = int(input('Введите число сдвига: '))
n_list = []
new_list = []

for _ in range(n):
    num = int(input('введите число: '))
    n_list.append(num)
    new_list.append(0)

for i in range(len(n_list)):
    if i + k >= len(n_list):
       new_list[i + k - len(n_list)] = n_list[i]
    else:
        new_list[i + k] = n_list[i]

print('Изначальный список:', n_list)
print('Сдвинутый список:', new_list)