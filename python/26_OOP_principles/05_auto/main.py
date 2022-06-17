# Задача не понятная!
# Условия размыты
"""Поэтому цена входа в автобус 25 р. и он городской=)))"""

import math


class Auto:
    dist = 0

    def __init__(self, x, y, fi):
        self.x = x
        self.y = y
        self.fi = fi

    def move(self, dist1, fi):
        self.x = self.x + dist1 * math.cos(fi)
        self.y = self.y + dist1 * math.sin(fi)
        self.dist += dist1

    def __str__(self):
        return f'ТС проехало {self.dist} км и находится в точке (x : {self.x} | y : {self.y})'


class Bus(Auto):
    count = 0
    money = 0

    def enter(self, qwt, tax=25):
        if self.count + qwt < 30:
            self.count += qwt
            self.money += tax * qwt
        elif self.count == 30:
            print('Мест нет!')
        else:
            r = 30 - self.count
            self.count += r
            self.money += r * tax

    def exit(self, qwt):
        if self.count >= qwt:
            self.count -= qwt
        else:
            print(f'в автобусе всего {self.count} переданное кол-во людей {qwt} больше (выходят все)')
            self.count = 0

    def __str__(self):
        inf = super().__str__()
        return f'\n{inf}\nВезет {self.count} людей\nВсего собрано денег {self.money}'


car = Auto(2, 5, 60)
car.move(250, 25)
car.move(350, 90)
print(car)

bus = Bus(0, 0, 90)
bus.move(240, 35)
bus.enter(25)
print(bus)
bus.move(260, 60)
bus.exit(26)
print(bus)
bus.enter(35)
print(bus)