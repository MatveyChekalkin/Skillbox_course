alphabet = ['а', 'о', 'у', 'э', 'ы', 'я',
            'ё', 'ю', 'е', 'и']

letters = [sym for sym in input('Введите текст: ')
           if sym in alphabet]
print(f'Список гласных букв: {letters}')
print(f'Список гласных букв: {len(letters)}')