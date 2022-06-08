quantity = int(input('Введите кол-во клеток: '))
cell_list = []
for i in range(1, quantity + 1):
    print('Эффективность', i, 'клетки:', end=' ')
    eff = int(input())
    if i > eff:
        cell_list.append(eff)
print('Неподходящие значения:', cell_list)
