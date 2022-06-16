import random


class Unit:
    health = 100

    def __init__(self, name):
        self.name = name


unit_1 = Unit('tiger')
unit_2 = Unit('woolf')

while unit_1.health != 0 and unit_2.health != 0:
    war = random.randint(1, 2)
    if war == 1:
        unit_2.health -= 20
        print(f'Бьёт {unit_1.name} (здоровье {unit_1.health}) по юниту {unit_2.name} (здоровье {unit_2.health})')
    else:
        unit_1.health -= 20
        print(f'Бьёт {unit_2.name} (здоровье {unit_2.health}) по юниту {unit_1.name} (здоровье {unit_1.health})')
else:
    print(f'{unit_1.name} побеждает') if unit_1.health > unit_2.health else print(f'{unit_2.name} побеждает')