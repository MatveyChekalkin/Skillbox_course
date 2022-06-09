def integer(text):
    for i in text:
        if not i.isdigit():
            return i

def summ(text):
    for i in text:
        if i.isdigit():
            if 0 > int(i):
                return int(i)
            elif 255 < int(i):
                return int(i)
        else:
            return 1
    return 1


text = input('Введите IP: ').split('.')
if len(text) != 4:
    print('Адрес - это четыре числа, разделенные точками ')

elif integer(text):
    print(f'{integer(text)} - не целое число')

elif 0 > summ(text) or summ(text) > 255:
    print(f'{summ(text)} - ниже 0 или превышает 255')
else:
    print('IP-адрес корректен')
