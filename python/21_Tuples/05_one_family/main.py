# Если я всё правильно понял

data = {
        ('Сидоров', 'Никита'): 35,
        ('Сидорова', 'Алина'): 34,
        ('Сидоров', 'Павел'): 10,
        ('Сидорович', 'Алина'): 34,
        ('Кукушкина', 'Павел'): 10
}

surname = input('Введите фамилию: ').lower()
for key, key_1 in data:
    if key.lower() == surname:
        print(key, key_1, data[(key, key_1)])
    elif surname == key.lower()[0:-1] or surname == key.lower() + 'а':
        print(key, key_1, data[(key, key_1)])

