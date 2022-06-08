qwt_friends = int(input('Кол-во друзей: '))
credit = int(input('Долговых расписок: '))
friends_list = []
for i in range(qwt_friends):
    i = [i + 1, 0]
    friends_list.append(i)

for i in range(credit):
    print(f'\n{i + 1} расписка')
    whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how = int(input('Сколько: '))
    friends_list[whom - 1][1] -= how
    friends_list[from_whom - 1][1] += how
print('\nБаланс друзей:')
for i in friends_list:
    print(i[0], ':', i[1])
