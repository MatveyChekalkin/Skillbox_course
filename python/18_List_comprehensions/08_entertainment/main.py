play_list = ['I' for i in range(int(input('Кол-во палок: ')))]
fight = int(input('Кол-во бросков: '))

for i in range(fight):
    print(f'Бросок {i + 1}. Сбиты палки с номерами: ', end=' ')
    L_i = int(input())
    print('по номер', end=' ')
    R_i = int(input())
    for i in range(0, len(play_list)):
        if i in range(L_i-1, R_i):
            play_list[i] = '.'
print(play_list)