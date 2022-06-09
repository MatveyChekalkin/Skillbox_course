qwt_chek = int(input('Введите кол-во заказов: '))
customer_dict = {}
data = []
name = set()
for i in range(1, qwt_chek + 1):
    data_str = input(f'{i} заказ: ').split()
    data.append(data_str)
    name.add(data_str[0])
    customer_dict[data_str[0]] = {}

for i in name:
    customer = {}
    piz = set()
    for b in data:
        if b[0] == i:
            if b[1] in piz:
                customer[b[1]] += int(b[2])
            else:
                customer[b[1]] = int(b[2])
                piz.add(b[1])
    customer_dict[i].update(customer)

for i in customer_dict:
    print(f'\n {i} :')
    for n in customer_dict[i]:
        print(f'        {n} : {customer_dict[i][n]}')

