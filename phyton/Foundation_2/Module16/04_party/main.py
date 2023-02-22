guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
choice = ''
while True:
    print(f'Сейчас на вечеринке {len(guests)} человек:', guests)
    while choice != 'пришел' and choice != 'ушел' and choice != 'пора спать':
        choice = input('Гость пришёл или ушёл? ')
        choice = choice.lower()
    if choice == "пора спать":
        print("Вечеринка закончилась, все легли спать.")
        break
    guest_name = input("Имя гостя: ")
    if choice == 'пришел':
        if len(guests) < 6:
            print("Привет,", guest_name)
            guests.append(guest_name)
        else:
            print(f'Прости, {guest_name}, но мест нет.')
    elif choice == 'ушел':
        if guest_name in guests:
            guests.remove(guest_name)
            print(f'Пока, {choice}!')
        else:
            print("Такого нет на вечеринке!")
    choice = ''
