import os

strings = 0

files = os.listdir()
for file in files:
    if os.path.isfile(file):
        if file.endswith('.py'):
            with open(file) as f:
                ss = f.read().split('\n')
                for s in ss:
                    if s.strip() and not s.startswith('#') and not s.startswith('"') and not s.startswith("'"):
                        strings += 1

print('Всего строк:', strings )