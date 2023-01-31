# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
name = ''
age = 0
phone = ''
email = ''
info = ''
postindex = 0
addres = ''
# busines info
ogrinp = 0
inn = 0
checking_account = 0
bank_name = ''
bik = 0
correspondent_account = 0

#Функция проверки вводимых данных на условие и возврат их (добавлена для контроля вводимых данных)
def check_and_input(type, length, comment):
  #type = 'd' - только цифры
  #       'l' - только символы
  #       's' - простой текст
  #length - длинна вводимых данных
  #comment - текст приглашения на ввод
  if (type != 'd' and type != 'l' and type != 's') or (isinstance(length, int) == False):
    print('Ошибка в параметрах!!!')
    return False
  while True:
    input_text = input(comment)
    if type == 'd':
      if input_text.isdigit() and len(input_text) == length:
        return int(input_text)
      else:
        print(f'\nОшибка ввода! Нужно ввести только цифры в количестве {length}, повторите ввод.\n')
    elif type == 'l':
      if input_text.isalpha() and len(input_text) <= length:
        return input_text
      else:
        print(f'\nОшибка ввода! Нужно ввести только буквы в количестве {length}, повторите ввод.\n')
    elif type == 's':
      if len(input_text) <= length:
        return input_text
      else:
        print(f'\nОшибка ввода! Нужно ввести текст длинной {length}, повторите ввод.\n')

def general_info(name, age, phone, email, info, postindex, addres):
  print(SEPARATOR)
  print('Имя:\t', name)
  if 11 <= age % 100 <= 19: 
    years_parameter = 'лет'
  elif age % 10 == 1: 
    years_parameter = 'год'
  elif 2 <= age % 10 <= 4: 
    years_parameter = 'года'
  else: 
    years_parameter = 'лет'
  print('Возраст:', age, years_parameter)
  print('Телефон:', phone)
  print('E-mail:\t', email)
  print('Индекс:\t', postindex)
  print('Адрес:\t', addres)
  print('Дополнительная информация:', info)

def busines_info(ogrnip, inn, checking_account, bank_name, bik, correspondent_account):
  print('\nИнформация о предпринимателе')
  print('ОГРИНП:\t', ogrinp)
  print('ИНН:\t', inn)
  print('Банковские реквизиты')
  print('Р/с:\t', checking_account)
  print('Банк:\t', bank_name)
  print('БИК:\t', bik)
  print('К/с:\t', correspondent_account)

def general_info_edit():
  global name
  global age
  global phone
  global email
  global info
  global postindex
  global addres
  name = check_and_input('s', 30, 'Введите имя: ')
  while True:
    # validate user age
    age = check_and_input('d', 2, 'Введите возраст: ')
    if age > 18:
      break
    print('Возраст должен быть положительным и больше 18 лет\n')
  phone = '+' + str(check_and_input('d', 11, 'Введите номер телефона (7ХХХХХХХХХХ): '))
  email = check_and_input('s', 40, 'Введите адрес электронной почты: ')
  postindex = check_and_input('d', 6, 'Введите почтовый индекс: ')
  addres = check_and_input('s', 80, 'Введите почтовый адрес: ')
  info = check_and_input('s', 80, 'Введите дополнительную информацию: ')

def busines_info_edit():
  global ogrinp
  global inn
  global checking_account
  global bank_name
  global bik
  global correspondent_account
  ogrinp = check_and_input('d', 15, 'ОГРНИП: ')
  inn = check_and_input('d', 20, 'ИНН: ')
  checking_account = check_and_input('d', 20, 'Расчетный счет: ')
  bank_name = check_and_input('l', 40, 'Название банка: ')
  bik = check_and_input('d', 6, 'БИК: ')
  correspondent_account = check_and_input('d', 20, 'Корреспондентский счет: ')

def edit_info():
  while True:
    print(SEPARATOR)
    print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
    print('1 - Лична информация')
    print('2 - Информация о предпринимателе')
    print('0 - Назад')
  
    option = check_and_input('d', 1, 'Введите номер пункта меню: ')
    if option == 0:
      break
    elif option == 1:
      # input general info
      general_info_edit()
    elif option == 2:
      # input busines info
      busines_info_edit()
    else:
      print('Введен некорректный пункт меню')
    
def print_info():
  while True:
    print(SEPARATOR)
    print('ВЫВЕСТИ ИНФОРМАЦИЮ')
    print('1 - Общая информация')
    print('2 - Вся информация')
    print('0 - Назад')

    option = check_and_input('d', 1, 'Введите номер пункта меню: ')
    if option == 0:
      break
    elif option == 1:
      general_info(name, age, phone, email, info, postindex, addres)
    elif option == 2:
      general_info(name, age, phone, email, info, postindex, addres)
      busines_info(ogrinp, inn, checking_account, bank_name, bik, correspondent_account)
      
    else:
      print('Введен некорректный пункт меню')


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
  # main menu
  print(SEPARATOR)
  print('ГЛАВНОЕ МЕНЮ')
  print('1 - Ввести или обновить информацию')
  print('2 - Вывести информацию')
  print('0 - Завершить работу')

  option = check_and_input('d', 1, 'Введите номер пункта меню: ')
  if option == 0:
    break
  if option == 1:
    # submenu 1: edit info
    edit_info()
  elif option == 2:
    # submenu 2: print info
    print_info()
  else:
    print('Введен некорректный пункт меню')
