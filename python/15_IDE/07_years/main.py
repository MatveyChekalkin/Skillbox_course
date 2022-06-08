def year(year_start,year_stop):
    for n in range(year_start, year_stop):
        if str(n)[0] == str(n)[1] == str(n)[2] \
                or str(n)[0] == str(n)[2] == str(n)[3] \
                or str(n)[0] == str(n)[1] == str(n)[3] \
                or str(n)[1] == str(n)[2] == str(n)[3]:
            print(n)

year_start = int(input('Введите первый год: '))
year_stop = int(input('Введите второй год: '))
if len(str(year_start)) != 4 or len(str(year_stop)) < 4:
    while len(str(year_start)) != 4 or len(str(year_stop)) < 4:
        print('ошибка ввода!, длина года не менее 4 символов')
        year_start = int(input('Введите первый год: '))
        year_stop = int(input('Введите второй год: '))
    year(year_start, year_stop)
else:
    year(year_start, year_stop)
