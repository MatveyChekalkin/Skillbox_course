row = []
class_1 = list(range(160, 176 + 1, 2))
class_2 = list(range(162, 180 + 1, 3))
row.extend(class_1)
row.extend(class_2)

print('Класс 1:', class_1)
print('Класс 2:', class_2)
row.sort()
print(row)
