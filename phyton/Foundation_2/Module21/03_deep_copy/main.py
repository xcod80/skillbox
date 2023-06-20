import copy

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
def print_site(new_site, name_site, level=0):
    for sub_key, sub_values in new_site.items():
        if isinstance(sub_values, str):
            new_site[sub_key] = new_site[sub_key].replace('телефон', name_site)
            new_site[sub_key] = new_site[sub_key].replace('iphone', name_site)
            print('\t'*level, '\'{}\' : \'{}\''.format(sub_key, new_site[sub_key]))
        elif isinstance(sub_values, dict):
            print('\t'*level, '\'{}\' :'.format(sub_key), '{')
            print_site(sub_values, name_site, level+1)
            print('\t'*(level+2), '},')
    return
site_nums = int(input('Сколько сайтов?: '))
for _ in range(site_nums):
    site_name = input('Введите название продукта для нового сайта: ')
    print(f'Сайт для {site_name}:')
    print('site = {')
    print_site(copy.deepcopy(site), site_name, 1)
    print('\t\t}')