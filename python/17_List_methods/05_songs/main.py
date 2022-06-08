violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

my_list =[]
qwt = int(input('Сколько песен выбрать? '))

for i in range(qwt):
    print('Название', i + 1,  'песни: ', end='')
    name = input()
    my_list.append(name)

summ = 0
for i in violator_songs:
    if i[0] in my_list:
        summ += i[1]

print('Общее время звучания песен:', round(summ,2), 'минут')