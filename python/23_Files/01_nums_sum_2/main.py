import os

char = []
summ = 0

file = open(os.path.abspath('numbers.txt'), 'r', encoding='utf-8')
for i_elem in file:
    char.extend(i_elem.split())
file.close()

for i in char:
    summ += int(i)

file_an = open(os.path.abspath('answer.txt'), 'w', encoding='utf-8')
file_an.write(str(summ))
file_an.close()

file_an = open(os.path.abspath('answer.txt'), 'r', encoding='utf-8')
file_answer = file_an.read()
file_an.close()

print(f'Содержимое файла answer.txt \n{file_answer}')