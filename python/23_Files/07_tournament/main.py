import os

first_tour = open(os.path.abspath('first_tour.txt'), 'w', encoding='utf-8')
first_tour.write('80\nIvanov Serg 80\nSegeev Petr 92\nPetrov Vasiliy 98\nVasiliev Maxim 78')
first_tour.close()

first_tour = open(os.path.abspath('first_tour.txt'), 'r', encoding='utf-8')
second_tour = open(os.path.abspath('second_tour.txt'), 'a', encoding='utf-8')
n = first_tour.readlines()
count = 0
second_tour_dict = {}

for i in n[1:]:
    if int(n[0]) < int(i.split()[-1]):
        second_tour_dict[int(i.split()[-1])] = i.split()[1][0] + '. ' + i.split()[0]
        count += 1
second_tour.write(str(count))

for key in sorted(second_tour_dict.keys(), reverse=True):
    second_tour.write(f'\n{second_tour_dict[key]} {str(key)}')

first_tour.close()
second_tour.close()