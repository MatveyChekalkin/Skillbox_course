class Parent:

    def __init__(self, name, age, child):
        self.name = name
        self.age = age
        self.child = [i for i in child if age - i.age > 16]
        self.child_list = [i.name if age - i.age > 16
                           else print(f'Ребенок {i.name} не может быть от родителя {name} ')
                           for i in child]

    def info(self):
        print(f'Имя: {self.name}\nВозвраст: {self.age} \nДети: {self.child_list}')

    def calm_ch(self, name):
        for i in self.child:
            if i.name == name:
                if i.calm != True:
                    i.calm = True
                    print(f'Родитель {self.name} успокоил ребенка {i.name}')
                else:
                    print(f'Ребенок {i.name} спокоен и успокаивать не требуется')

    def hunger_ch(self, name):
        for i in self.child:
            if i.name == name:
                if i.hunger != True:
                    i.hunger = True
                    print(f'Родитель {self.name} накормил ребенка {i.name}')
                else:
                    print(f'Ребенок {i.name} не голоден и кормить не требуется')


class Children:

    def __init__(self, name, age, calm=False, hunger=False):
        self.name = name
        self.age = age
        self.calm = calm
        self.hunger = hunger


ch1 = Children('Alex', 8, True)
ch2 = Children('Bob', 10, False, True)
ch3 = Children('Tom', 56)
mother2 = Parent('Alice', 40, [ch3])
father = Parent('Dima', 35, [ch1, ch2])
mother = Parent('Anna', 30, [ch1, ch2])
father.info()
mother.info()
mother2.info()
father.calm_ch('Alex')
father.calm_ch('Bob')
mother.calm_ch('Bob')
father.hunger_ch('Alex')
mother.hunger_ch('Alex')
mother.hunger_ch('Bob')