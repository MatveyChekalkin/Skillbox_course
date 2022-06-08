rollers_list = []
people_list = []

rollers_qwt = int(input('Кол-во коньков: '))
for i in range(rollers_qwt):
    print(f'Размер {i + 1} пары: ', end='')
    rollers = int(input())
    rollers_list.append(rollers)

people_qwt = int(input('Кол-во людей: '))
for i in range(people_qwt):
    print(f'Размер ноги  {i + 1} человека: ', end='')
    people = int(input())
    people_list.append(people)

count = 0
for i in people_list:
    if i <= max(rollers_list):
        count += 1
        rollers_list.remove(max(rollers_list))

print(f'Наибольшее кол-во людей, которые могут взять ролики: {count}')