violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

qwt_music = int(input('Сколько песен выбрать? '))
summ_time = 0
for i in range(1, qwt_music + 1):
    summ_time += violator_songs.get(input(f'Название {i} песни: '), 0)
print(f'Общее время звучания песен: {round(summ_time, 2)} минут')
