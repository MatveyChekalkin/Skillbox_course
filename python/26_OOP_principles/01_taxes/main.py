# Задача не очень! условия размыты и непонятны! такое и решение=)
class Property:
    taxx = 0

    def __init__(self, name, worth):
        self.name = name
        self.worth = worth

    def tax(self):
        pass

    def __str__(self):
        return f'Имущество: {self.name}\nНалогооблагаемая база: {self.worth}'


class Apartment(Property):

    def tax(self):
        self.taxx = self.worth / 1000

    def __str__(self):
        info = super().__str__()
        return f'{info}\nСумма налога: {self.taxx}\n'


class Car(Property):

    def tax(self):
        self.taxx = self.worth / 200

    def __str__(self):
        info = super().__str__()
        return f'{info}\nСумма налога: {self.taxx}\n'


class CountryHouse(Property):

    def tax(self):
        self.taxx = self.worth / 500

    def __str__(self):
        info = super().__str__()
        return f'{info}\nСумма налога: {self.taxx}\n'


apart = Apartment(name='Квартира', worth=10000000)
car = Car(name='Машина', worth=500000)
house = CountryHouse(name='Дом', worth=2500000)

money = int(input('Введите кол-во имеющихся денег: '))

for i in apart, car, house:
    i.tax()
    print(i)
    if money < i.taxx:
        print(f'Недостаточно средств, чтобы оплатить налог на {i.name}')
        break
    else:
        money -= i.taxx
        print(f'Денег осталось после оплаты налога {money}\n')