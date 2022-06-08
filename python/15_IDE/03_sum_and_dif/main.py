def summ(number):
    summ = 0
    for n in range(int(len(str(number)))):
        a = str(number)[n]
        summ += int(a)
    return summ

def leghn(number):
    return int(len(str(number)))

number = int(input('Введите число: '))

print('Сумма чисел:', summ(number))
print('Кол-во цифр в числе:', leghn(number)) # Можно и без функции int(len(str(number)))
print('Разность суммы и кол-ва цифр:', summ(number) - leghn(number))