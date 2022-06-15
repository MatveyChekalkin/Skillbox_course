import os

# with open(os.path.abspath('people.txt'), 'a', encoding='utf-8') as people_file: # Ссоздается файл
#     while True:
#         try:
#             qwt = int(input('Колво имен: '))
#         except ValueError:
#             print(f'тип не int')
#         else:
#             break
#     for _ in range(0, qwt):
#         people_file.write(input(f'\nВведите имя: ')+'\n')

with open(os.path.abspath('people.txt'), 'r', encoding='utf-8') as file:
    sum_symb = 0
    for i, elem in enumerate(file.read().split()):
        try:
            if len(elem) < 3:
                raise IndexError
            elif not elem.isalpha():
                raise TypeError
        except IndexError:
            print(f'Длина имени в {i + 1} строке меньше 3 символов')
            with open(os.path.abspath('errors.log'), 'a', encoding='utf-8') as errors_log:
                errors_log.write(f'Длина имени в {i + 1} строке меньше 3 символов\n')
        except TypeError:
            print(f'Имя в {i + 1} строке содержит символы не из алфавита')
            with open(os.path.abspath('errors.log'), 'a', encoding='utf-8') as errors_log:
                errors_log.write(f'Имя в {i + 1} строке содержит символы не из алфавита\n')
        else:
            sum_symb += len(elem)

print(f'Общая сумма: {sum_symb}')

