class Awg:
    awg_list = []


class Student:

    def __init__(self, name, sur, num, qwt=5):
        self.last_name = name
        self.sur_name = sur
        self.number = num
        self.greats = [int(input(f'По студенту {name} введите {i + 1} оценку: ')) for i in range(qwt)]
        self.awg = sum(self.greats) / qwt
        Awg.awg_list.append(self.awg)

    def info(self):
        print(f'Имя: {self.last_name} \nФамилия: {self.sur_name} '
              f'\nГруппа: {self.number} \nОценки: {self.greats}'
              f'\nСредняя: {self.awg}\n')


st1 = Student('bob', 'li', 56)
st2 = Student('Alice', 'by', 58)
st3 = Student('Alex', 'ti', 36)

for i_elem in sorted(Awg.awg_list, reverse=True):
    for n in st1, st2, st3:
        if n.awg == i_elem:
            n.info()