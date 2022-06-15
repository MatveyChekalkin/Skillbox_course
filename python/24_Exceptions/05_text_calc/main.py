import os

# with open(os.path.abspath('calc.txt'), 'w', encoding='utf-8') as file:
#     for i in range(int(input('Кол-во операций: '))):
#         file.write(input(f'Введите {i + 1} операцию: ')+'\n')

def operation(elem):
    try:
        res = eval(elem)
    except ZeroDivisionError:
        return 'На ноль делить нелзя'
    except (NameError, SyntaxError):
        return 'Введена буква'
    else:
        return res

with open(os.path.abspath('calc.txt'), 'r', encoding='utf-8') as file:
    summ_nums = 0
    for i, elem in enumerate(file.read().split('\n')):
        res = operation(elem)
        if isinstance(res, int) or isinstance(res, float):
            summ_nums += res
        else:
            print(f'в {i} строке ошибка ({res})')
    print(summ_nums)