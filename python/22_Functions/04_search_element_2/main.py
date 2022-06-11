site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}

def key_searhc(site,key, deep=2):
	if key in site:
		return site[key]
	elif deep == 0:
		return None

	for element in site.values():
		if isinstance(element, dict):
			res = key_searhc(element, key, deep - 1)
			if res:
				break
	else:
		res = None

	return res



key = input('Введите ключ: ').lower()
deep = int(input('Выбирите глубину поиска (по умолчанию максимальная глубина 2): '))
res = key_searhc(site,key,deep)
if res:
	print(res)
else:
	print('Такого ключа нет')

