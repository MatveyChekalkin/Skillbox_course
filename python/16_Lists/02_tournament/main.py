name_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
firs_day = []
second_day = []

for i in range(len(name_list)):
    if (i + 1) % 2 == 0:
        firs_day.append(name_list[i])
    else:
        second_day.append(name_list[i])

print('Команда на первый день:', firs_day)
print('Команда на второй день:', second_day)