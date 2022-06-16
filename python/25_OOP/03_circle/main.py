import math


class Circle:

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def s_circle(self):
        print(f'Площадь окружности: {math.pi * self.r ** 2}')

    def p_circle(self):
        print(f'Площадь окружности: {2 * math.pi * self.r}')

    def increase_circle(self, k=1):
        self.r *= k
        print(f'Окружность увеличенна в {k} раз'
              f'\nНовый радиус равен: {self.r}')

    def is_intersectdef(self, cir):
        if self.x == cir.x:
            if self.r + cir.r > abs(self.y - cir.y):
                print('Окружности пересекаются')
            else:
                print('Окружности не пересекаются')
        elif self.y == cir.y:
            if self.r + cir.r > abs(self.x - cir.x):
                print('Окружности пересекаются')
            else:
                print('Окружности не пересекаются')
        else:
            if (self.r + cir.r) ** 2 > abs((self.x - cir.x) ** 2 - (self.y - cir.y) ** 2):
                print('Окружности пересекаются')
            else:
                print('Окружности не пересекаются')


cir1 = Circle(1, 1, 4)
cir1.s_circle()
cir1.p_circle()
cir1.increase_circle(1)

cir2 = Circle()
cir2.s_circle()
cir2.p_circle()
cir2.increase_circle(6)
cir2.s_circle()
cir2.p_circle()
cir1.is_intersectdef(cir2)