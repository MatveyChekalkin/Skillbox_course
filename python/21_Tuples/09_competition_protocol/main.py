def score_key(a):
    return a[1][0]*100000000 - a[1][1]

score_table = {}
N = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя): ')
for time in range(N):
    ball, name = input(f'{time + 1} запись: ').split()
    ball = int(ball)
    if name in score_table:
        if ball > score_table[name][0]:
            score_table[name][0] = ball
            score_table[name][1] = time
    else:
        score_table[name] = [ball, time]

scores = list(score_table.items())
scores.sort(key=score_key, reverse = True)

print('\nИтоги соревнований:')
for winner_index in 0, 1, 2:
    print(winner_index + 1, 'место.', scores[winner_index][0], end =' ')
    print('(', scores[winner_index][1][0], ')', sep='')