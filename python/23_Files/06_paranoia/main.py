import os

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
         'h', 'i', 'j', 'k', 'l',
         'm', 'n', 'o', 'p', 'q', 'r', 's',
         't', 'u', 'v', 'w', 'x', 'y', 'z']

file = open(os.path.abspath('text.txt'), 'w', encoding='utf-8')
file.write('Hello\n' * 4)
file.close()

file = open(os.path.abspath('text.txt'), 'r', encoding='utf-8')
new_file = open(os.path.abspath('cipher_text.txt'), 'w', encoding='utf-8')
row = ''
for i, elem in enumerate(file):
    for a in range(len(elem)):
        if str(elem[a]).lower() in alpha:
            if alpha.index(str(elem[a]).lower()) + 1 + i >= 26:
                row += alpha[alpha.index(str(elem[a]).lower()) + 1 + i - 26]
            else:
                row += alpha[alpha.index(str(elem[a]).lower()) + 1 + i]
        else:
            row += str(elem[a]).lower()
new_file.write(row.title())
new_file.close()
file.close()