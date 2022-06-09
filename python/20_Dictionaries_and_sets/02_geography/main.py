country_dict = dict()

country = int(input('Кол-во стран: '))
for i in range(1, country + 1):
    list_city = list(input(f'{i} страна: ').split())
    country_dict[list_city[0]] = list_city[1:]

for i in range(1, 3 + 1):
    city = input(f'{i} город: ')
    count = 0 # Костыль
    for key in country_dict:
        if city in country_dict.get(key):
            print(f'Город {city} расположен в стране {key}.')
            count = 0 # Костыль
            break
        else: # Костыль
            count += 1 # Костыль
        if count == country: # Костыль
            print(f'По городу {city} данных нет.') # Костыль