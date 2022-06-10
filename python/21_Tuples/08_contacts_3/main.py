def enter(contact):
    user = input('\nвведите Имя и фамилию через пробел: ').split()
    if (user[1].lower(), user[0].lower()) in contact.keys():
        print('Этот человек уже есть в списке контактов')
        enter(contact) # Рекурсия
    else:
        num_phone = int(input('Введите номер телефона: '))
        contact[(user[1].lower(), user[0].lower())] = num_phone

def search(contact):
    surname = input('\nВведите фамилию: ').lower()
    for key, key_1 in contact:
        if key.lower() == surname:
            print(key, key_1, contact[(key, key_1)])
        elif surname == key.lower()[0:-1] or surname == key.lower() + 'а':
            print(key, key_1, contact[(key, key_1)])


contact = dict()

while True:
    answer = input('\nВыбирите действие (Добавить или Нaйти или Выход): ').lower()
    if answer == 'добавить':
        enter(contact)
        print(contact)
    elif answer == 'найти':
        search(contact)
    elif answer == 'выход':
        print('\nДосвидание! \nВыход из программы')
        break
    else:
        print('\nОшибка ввода')



