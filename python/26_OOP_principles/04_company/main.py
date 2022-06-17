class Person:
    def __init__(self, name, last_name, ade):
        self.__name = name
        self.__last_name = last_name
        self.__age = ade

    def get_name(self):
        return self.__name

    def get_last_name(self):
        return self.__last_name

    def get_age(self):
        return self.__age

    def __str__(self):
        return f'Имя: {self.get_name()} Фамилия: {self.get_last_name()} Возраст: {self.get_age()}'


class Employee(Person):
    def calc_salary(self):
        pass

    def __str__(self):
        inf = super().__str__()
        return f'{inf}\nЗ/п: {self.calc_salary()}\n'


class Manager(Employee):
    def calc_salary(self):
        return 13000


class Agent(Employee):
    qwt = 2156 # можно было сделать у всех разное, но задание не очень поэтому пусть будет так

    def calc_salary(self):
        return 5000 + self.qwt * 0.05


class Worker(Employee):
    hours = 200 # можно было сделать у всех разное, но задание не очень поэтому пусть будет так

    def calc_salary(self):
        return 100 * self.hours


employee_list = []

name_list = ['Мария', 'Оля', 'Рита', 'Леша', 'Паша', 'Саша', 'Сеня', 'Ира', 'Сергей']
last_name_list = ['Иванова', 'Петрова', 'Зябликова', 'Кукушкин', 'Ли', 'Иванов', 'Петров', 'Ли', 'Уткин']
age_list = [25, 30, 45, 20, 23, 25, 40, 50, 31]
for i in range(3):
    employee_list.append(Manager(name=name_list[i], last_name=last_name_list[i], ade=age_list[i]))

for i in range(3, 6):
    employee_list.append(Agent(name=name_list[i], last_name=last_name_list[i], ade=age_list[i]))

for i in range(6, 9):
    employee_list.append(Worker(name=name_list[i], last_name=last_name_list[i], ade=age_list[i]))

for i in employee_list:
    print(i)
