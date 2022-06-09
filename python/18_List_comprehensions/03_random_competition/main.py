import random as r

fst_groop = [round(r.uniform(5, 10), 2) for _ in range(10)]
snd_groop = [round(r.uniform(5, 10), 2) for _ in range(10)]

winner = [(fst_groop[i] if fst_groop[i] > snd_groop[i] else snd_groop[i]) for i in range(10)]
print(f'Первая команда: {fst_groop}')
print(f'Вторая команда: {snd_groop}')
print(f'Победители тура: {winner}')
