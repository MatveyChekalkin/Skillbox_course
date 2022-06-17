import random
import os


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day():
    try:
        if random.randint(1, 10) == 10:
            error = random.choice(['KillError', 'DrunkError',
                                   'CarCrashError', 'GluttonyError', 'DepressionError'])
            raise eval(error)
    except eval(error):
        with open(os.path.abspath('karma.log'), 'a', encoding='utf-8') as file:
            file.write(f'{error}\n')
        scored = 0
    else:
        scored = random.randint(1, 7)
    return scored


score = 0
day = 0
while True:
    if score >= 500:
        print(f'\n               Победа\nНа день {day} набрано нужное кол-во {score} очков.')
        break
    day += 1
    score_day = one_day()
    score += score_day
    print(f'день {day} очки за день {score_day} всего очков {score}')



