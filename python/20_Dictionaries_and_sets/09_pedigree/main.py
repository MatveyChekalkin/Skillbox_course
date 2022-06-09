dict_tree = dict()

qwt_people = int(input('Введите количество человек: '))
for i in range(qwt_people - 1):
    two = input(f'{i + 1} пара: ').split()
    if two[1] not in dict_tree:
        dict_tree[two[1]] = i
    if two[1] in dict_tree:
        dict_tree[two[0]] = dict_tree[two[1]] + 1

print('\n“Высота” каждого члена семьи:')
for key in sorted(dict_tree):
    print(f'{key} : {dict_tree[key]}')