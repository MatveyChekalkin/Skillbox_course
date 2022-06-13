import os

text = open(os.path.abspath('text.txt'), 'w', encoding='utf-8')
text.write('Mama myla ramu.')
text.close()

text = open(os.path.abspath('text.txt'), 'r', encoding='utf-8')
analysis = open(os.path.abspath('analysis.txt'), 'a', encoding='utf-8')
file = text.readline()
file_str = file.replace(' ', '').replace('.', '').lower()
analysis_dict = {}
for i in set(file_str):
    num = round(file_str.count(i) / len(file_str), 3)
    if num in analysis_dict.keys():
        analysis_dict[num].append(i)
        analysis_dict[num].sort()
    else:
        analysis_dict[num] = list(i)
for i in sorted(analysis_dict.keys(), reverse=True):
    for values in analysis_dict[i]:
        analysis.write(f'{values}  {str(i)}\n')

analysis.close()
text.close()
