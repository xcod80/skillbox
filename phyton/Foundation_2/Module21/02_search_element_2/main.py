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

def search_key(user_dict, user_key, deep=-1):
	if deep !=0:
		if user_key in user_dict:
			return user_dict[user_key]
		for sub_dict in user_dict.values():
			if isinstance(sub_dict, dict):
				sub_search = search_key(sub_dict, user_key, deep - 1)
				if sub_search != None:
					return sub_search
	return None
my_key = input('Введите искомый ключ: ')
if input('Хотите ввести максимальную глубину? (Y/n)').lower() == 'y':
	my_deep = int(input('Введите максимальную глубину: '))
	print('Значение ключа: ', search_key(site, my_key, my_deep))
else:
	print('Значение ключа: ', search_key(site, my_key))
