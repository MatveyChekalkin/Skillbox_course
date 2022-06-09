text = list(input('Введите строку: '))
sym_set = set()
for i in text:
    if i in sym_set:
        sym_set.remove(i)
    else:
        sym_set.add(i)
if len(sym_set) > 1:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')

