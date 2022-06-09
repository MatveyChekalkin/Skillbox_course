fst_str = list(input('Первая строка: '))
scd_str = list(input('Вторая строка: '))
fst_cop = fst_str.copy()

for i in range(0, len(fst_str)):
    fst_cop[i] = fst_str[(i + abs(0-fst_str.index(scd_str[0]))) % len(fst_str)]
if fst_cop == scd_str:
    print(f'Первая строка получается из второй со сдвигом {abs(0-fst_str.index(scd_str[0]))}.')
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')