word = input('Введите слово: ')
if word[::-1] == word:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')