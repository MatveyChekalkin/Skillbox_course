while True:
    password = input('Придумайте пароль: ')
    num = [int(x) for x in password if x.isdigit()]
    if len(password)>7 and not password.islower() and len(num) >= 3:
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')

