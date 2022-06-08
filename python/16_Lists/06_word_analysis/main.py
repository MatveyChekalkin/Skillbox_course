word = input('Введите слово: ')
word_list = list(word)
unique = 0

for symbol in word_list:
    count = 0
    for i in word_list:
        if symbol == i:
            count += 1
    if count < 2:
        unique += 1

print(unique)