import os
import random

file_path = open(os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt')), 'r', encoding='utf-8')
file = ''.join(file_path.read().replace(' ', '').replace(',', '').replace('--', '').replace('*', '').replace("'",'')\
    .replace('.', '').replace('!', '').split('\n'))
print(f'Кол-во букв латинского алфавита: {len(file)}')
file_path.close()

file_path = open(os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt')), 'r', encoding='utf-8')
file = ''.join(file_path.read().replace(',', '').replace('--', '').replace('*', '').replace("'",'')\
    .replace('.', '').replace('!', '').split('\n')).split(' ')
print(f'Кол-во слов: {len(file)}')
file_path.close()

file_path = open(os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt')), 'r', encoding='utf-8')
file = file_path.readlines()
print(f'Кол-во строк: {len(file)}')
file_path.close()

file_path = open(os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt')), 'r', encoding='utf-8')
file = ''.join(file_path.read().replace(' ', '').replace(',', '').replace('--', '').replace('*', '').replace("'",'')\
    .replace('.', '').replace('!', '').split('\n')).lower()
unic_alpf=list(set(file))
mina_alph = file.count(random.choice(unic_alpf))
alph =''
for elem in unic_alpf:
    if mina_alph >= file.count(elem):
        mina_alph = file.count(elem)
        alph = elem
print(f'минимальное количество ({mina_alph}) встречается буква - {alph}')
file_path.close()
