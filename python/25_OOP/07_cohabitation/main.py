import random


class Human:

    def __init__(self, name, satiety=50, food=50, money=0):
        self.name = name
        self.satiety = satiety
        self.food = food
        self.money = money

    def day(self, action):
        if self.satiety < 20 and self.food >= 10:
            self.satiety += 10
            self.food -= 10
            print(f'{self.name} поел')
        elif self.food < 10 and self.money > 0:
            self.food += 20
            self.money -=10
            print(f'{self.name} сходил в магазин')
        elif action == 1:
            self.money += 50
            print(f'{self.name} работает')
        elif action == 2:
            self.satiety += 10
            self.food -= 10
            print(f'{self.name} ест')
        else:
            self.satiety -= 10
            print(f'{self.name} играет')


class Result:
    def __init__(self, man, woman):
        self.man = man
        self.woman = woman

    def life_death(self):
        if self.man.satiety == 0 or self.woman.satiety == 0:
            return True, print('Один из участников умер')


man = Human('Ваня')
woman = Human('Маша')

result = Result(man, woman)
count_day = 0

while True:
    count_day += 1
    if count_day == 365:
        print('\n Все живы, удачный эксперемент')
        break
    elif result.life_death():
        break
    else:
        r = random.randint(1, 6)
        man.day(r)
        woman.day(r)