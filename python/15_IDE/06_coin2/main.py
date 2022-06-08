def money(x,y,R):
    if (x ** 2 + y ** 2) <= R ** 2:
        return print('Монетка где-то рядом')
    else:
        return print('Монетки нет рядом')

x,y, R = float(input('X: ')), float(input('Y: ')),float(input('Введите радиус: '))
money(x,y,R)