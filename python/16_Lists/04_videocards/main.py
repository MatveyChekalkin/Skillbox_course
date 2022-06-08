qwt_card = int(input('Кол-во видеокарт: '))
card_list = []
new_card_list = []

for i in range(qwt_card):
    print(i + 1, 'Видеокарта:', end=' ')
    card = int(input())
    card_list.append(card)

for card in card_list:
    if card != max(card_list):
        new_card_list.append(card)

print('Старый список видеокарт:', card_list)
print('Новый список видеокарт:', new_card_list)
