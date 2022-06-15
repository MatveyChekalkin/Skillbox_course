import random
import os

errors = [SystemError,TypeError,ValueError,KeyError,IndexError]
summ = 0
try:
    while 777 > summ:
        user_num = int(input('Введите число: '))
        if 13 == random.randint(1, 13):
            raise random.choice(errors)
        summ += user_num
        with open(os.path.abspath('nums.txt'), 'a', encoding='utf-8') as file:
            file.write(str(user_num) + '\n')
except Exception:
    print('Неведомая ошибка')
else:
    print('Победа')


