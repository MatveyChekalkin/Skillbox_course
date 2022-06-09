word_dict = dict()
word_qwt = int(input('Введите количество пар слов: '))
for i in range(1, word_qwt + 1):
   two = input(f'{i} пара: ').lower().split(' - ')
   word_dict[two[0]] = two[1]

while True:
    word = input('\nВведите слово: ').lower()
    if word in word_dict.keys():
        print(f'Синоним: {word_dict.get(word)}')
        break
    elif word in word_dict.values():
        for i in word_dict.keys():
            if word_dict[i] == word:
                print(f'Синоним: {i}')
        break
    else:
        print('Такого слова в словаре нет.')


