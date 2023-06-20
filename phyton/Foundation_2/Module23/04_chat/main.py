def see_chat():
    with open('chat.txt', 'r', encoding='utf8') as chat_file:
        item = chat_file.read().split('\n')
        for line in item[-10::]:
            print(line)
    return

def send_message(name, mess):
    with open('chat.txt', 'a', encoding='utf8') as chat_file:
        chat_file.write(f'{name}\t{mess}\n')
    return

name = input('Введите имя:')
while True:
    print()
    print('1 - Просмотреть текст чата')
    print('2 - Отправить сообщение в чат')
    print('0 - Покинуть чат')
    try:
        sel = int(input())
        if sel > 2:
            raise ValueError
    except ValueError:
        print('Для выбора введите целое число.')
    else:
        if sel == 1:
            see_chat()
        elif sel == 2:
            send_message(name, input('Введите сообщение: '))
            see_chat()
        elif sel == 0:
            print('До встречи!!!')
            exit()