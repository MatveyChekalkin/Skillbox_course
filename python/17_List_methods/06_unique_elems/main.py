def list_enter(x, a_list):
    print(f'\nДля списка из {x} чисел.')
    for _ in range(x):
        num = int(input('Введите число: '))
        a_list.append(num)

first_list = []
second_list = []
list_enter(3,  first_list)
list_enter(7,  second_list)
first_list.extend(second_list)

for i in first_list:
    while first_list.count(i) != 1:
        first_list.remove(i)

print(first_list)

