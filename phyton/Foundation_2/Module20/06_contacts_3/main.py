contact_list = {('Иван', 'Сидоров'):888}
def search_contact(in_family, contacts):
    exit_contact = dict()
    for name, family in contacts:
        if in_family == family:
            exit_contact[tuple([name, family])] = contacts[name, family]
    if len(exit_contact) < 1:
        return False
    else:
        return exit_contact
def add_contact(contacts):
    while True:
        try:
            name, family = input('Введите имя и фамилию нового контакта (через пробел): ').title().split()
            if tuple([name, family]) in contacts:
                print('Такой человек уже есть в контактах')
                break
            phone_number = input('Введите номер телефона: ')
        except Exception:
            print('Ощибка ввода, повторите ввод')
        contacts[tuple([name, family])] = phone_number
        break
    return

while True:
    print('\n')
    print('Текущий словарь контактов:', contact_list)
    print('\n')
    print('1 - Поиск контакта')
    print('2 - Добавить контакт')
    print('3 - Выход')
    try:
        choice = int(input())
    except Exception:
        print('Повторите ввод.')
        continue
    if choice == 3:
        break
    elif choice == 2:
        add_contact(contact_list)
    elif choice ==1:
        find_data = search_contact(input('Введите фамилию для поиска: ').title(), contact_list)
        if not find_data :
            print('Такого человека нет в справочнике.')
        else:
            for find_name, find_family in find_data:
                print(find_name, find_family, find_data[(find_name, find_family)])
