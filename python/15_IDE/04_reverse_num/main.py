def rev(f, s):
    rev1 = str(f)[::-1]
    rev2 = str(s)[::-1]
    return float(rev1 + '.' + rev2)

fnum, fsnum = input('Введите первое число: ').split('.')
snum, ssnum = input('Введите первое число: ').split('.')
fnum = rev(fnum, fsnum)
snum = rev(snum, ssnum)
print('Первое число наоборот:', fnum)
print('Второе число наоборот:', snum)
print('Сумма:', fnum + snum)