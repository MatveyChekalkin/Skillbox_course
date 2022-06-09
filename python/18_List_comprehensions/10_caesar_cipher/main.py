alpha = ['а', 'б', 'в', 'г', 'д', 'е', 'ё',
         'ж', 'з', 'и', 'й', 'к',
         'л', 'м', 'н', 'о', 'п', 'р', 'с',
         'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш',
         'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

text =[x for x in input('введите текст: ')]
row = ''
for i in range(len(text)):
    if text[i] in alpha:
        if alpha.index(text[i]) + 3 >= 33:
            row += alpha[alpha.index(text[i]) + 3 - 33]
        else:
            row += alpha[alpha.index(text[i]) + 3]
    else:
        row += text[i]
print(row)