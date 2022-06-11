site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

def sructure(site, name):
    if 'title' in site:
        site['title'] = f'Куплю/продам {name} недорого'
    if 'h2' in site:
        site['h2'] = f'У нас самая низкая цена на {name}'

    for key in site.values():
        if isinstance(key,dict):
            sructure(key, name)
    return site
qwt_site = int(input('Сколько сайтов: '))

for _ in range(qwt_site):
    product_name = input('Введите название продукта для нового сайта: ')
    print(f'Сайт для {product_name}')
    print(f'site = {sructure(site.copy(),product_name)}')

