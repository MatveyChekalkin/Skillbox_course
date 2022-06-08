def delit(number):
    answer = 0
    for n in range(2, number + 1):
       if number % n == 0:
           answer = n
           break
    return answer

number = int(input('Введите число(n>1): '))
if number <= 1:
    while number <= 1:
        print('Ошибка ввода')
        number = int(input('Введите число(n>1): '))
    print('Наименьший делитель, отличный от единицы:', delit(number))
else:
   print('Наименьший делитель, отличный от единицы:', delit(number))