n = int(input('Введите кол-во элементов в списке: '))
list_n = []
sort_list_n = []
list_n_s = []

for _ in range(n):
    number = int(input('Введите число: '))
    list_n.append(number)
    list_n_s.append(number)

while list_n_s != []:
    sort_list_n.append(min(list_n_s))
    list_n_s.remove(min(list_n_s))

print('Изначальный список:', list_n)
print('\n Отсортированный список:', sort_list_n)
print('Отсортированный список:', sorted(list_n))
