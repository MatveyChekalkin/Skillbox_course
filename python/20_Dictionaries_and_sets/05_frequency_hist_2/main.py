# Здесь что-то написано
text = input('Введите текст: ')
text_dict = dict()
for sym in text:
    if sym in text_dict:
        text_dict[sym] += 1
    else:
        text_dict[sym] = 1

print('Оригинальный словарь частот:')
for key in sorted(text_dict.keys()):
    print(f'{key} : {text_dict[key]}')


new_dict = dict()
for i in set(text_dict.values()):
    new_dict[i] = []

for sym, qwt in text_dict.items():
    for i in new_dict:
        if qwt == i:
            new_dict[i].append(sym)

print('Инвертированный словарь частот: ')
for i in new_dict:
    print(f'{i} : {new_dict[i]}')