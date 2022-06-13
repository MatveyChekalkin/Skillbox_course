import os

file_path = open(os.path.abspath('zen.txt'), 'r', encoding='utf-8')
rev = dict()
for i, i_element in enumerate(file_path):
    rev[i] = i_element[0:-1]
file_path.close()

for i_element in sorted(rev.keys(), reverse=True):
    print(rev[i_element])

# file_path = open(os.path.abspath('zen.txt'), 'r', encoding='utf-8')
# file = file_path.readlines()
# file.reverse()
# print(''.join(file))
# file_path.close()
