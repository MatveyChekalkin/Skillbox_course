guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    run = input('Гость пришел или ушел? ')
    name = input('Имя гостя: ')
    if run == 'пришел':
        if len(guests) == 6:
            print('Прости,', name,', но мест нет.')
        else:
            print('Привет,', name)
            guests.append(name)
    elif run == 'ушел':
        print('Пока,', name,'!')
        guests.remove(name)
    elif run == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break