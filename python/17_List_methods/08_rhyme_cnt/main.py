qwt_people = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {number} человек')
const = [number]
play_list = list(range(1, qwt_people + 1))


while True:
    print(f'\nТекущий круг людей: {play_list}')
    number_start = int(input('Начало счёта с номера: '))
    while len(play_list[play_list.index(number_start):]) < number:
        number -= len(play_list[play_list.index(number_start):])
        if number <= len(play_list):
            print(f'Выбывает человек под номером {play_list[number-1]}')
            play_list.remove(play_list[number-1])
            number = const[0]
            break
    if len(play_list) == 1:
        print(f'\nОстался человек под номером {play_list[0]}')
        break