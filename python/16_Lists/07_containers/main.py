def koef(container_list):
    count = 0
    for koef in container_list:
        if koef == x:
            count += 1
    return count


def enter(container):
    if 0 >= container or 200 <= container:
        while 0 >= container or container >= 200:
            print('Ошибка ввода, вес контейнера больше 0 и меньше 200')
            container = int(input('Введите вес контейнера: '))
        return container_list.append(container)
    else:
        return container_list.append(container)

container_qwt = int(input('Кол-во контейнеров: '))
container_list = []
for _ in range(container_qwt):
    container = int(input('Введите вес контейнера: '))
    enter(container)

x = int(input('Введите вес нового контейнера:'))
enter(x)
x = container_list[len(container_list) - 1]

print(sorted(container_list, reverse=True))
print('Номер, куда встанет новый контейнер:', sorted(container_list, reverse=True).index(x) + 1 * koef(container_list))
