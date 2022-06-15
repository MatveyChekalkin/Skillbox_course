import os

def errors(i, lines, text_er):
    with open(os.path.abspath('registrations_bad.log'), 'a', encoding='utf-8') as file_bad:
        file_bad.write(f'Ошибка в {i + 1} строке! Текст ошибки: {text_er}  ({lines})\n')

def check(lines, i):
    try:
        if len(lines) != 3:
            raise IndexError
        elif not lines[0].isalpha():
            raise NameError
        elif '@' not in lines[1] and '.' not in lines[1]:
            raise SyntaxError
        elif 10 > int(lines[2]) or int(lines[2]) > 99:
            raise ValueError
    except IndexError:
        errors(i, lines, 'НЕ присутствуют все три поля')
    except NameError:
        errors(i, lines, 'поле имени содержит НЕ только буквы')
    except SyntaxError:
        errors(i, lines, 'поле емейл НЕ содержит @ и .(точку)')
    except ValueError:
        errors(i, lines, 'поле возраст НЕ является числом от 10 до 99')
    else:
        with open(os.path.abspath('registrations_good.log'), 'a', encoding='utf-8') as file_good:
            file_good.write(' '.join(lines) + '\n')

with open(os.path.abspath('registrations.txt'), 'r', encoding='utf-8') as file:
    for i, line in enumerate(file):
        check(line.split(), i)
