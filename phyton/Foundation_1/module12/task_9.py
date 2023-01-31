print('Задача 9. Недоделка')

# Вы пришли на работу в контору по разработке игр,
# целевая аудитория которых - дети и их родители.
# 
# У прошлого программиста было задание
# сделать две игры в одном приложении, чтобы пользователь мог выбирать одну из них.
# 
# Однако программист, на место которого вы пришл
# и, перед увольнением не успел сделать эту задачу и оставил только небольшой шаблон проекта.
# 
# Используя этот шаблон,
# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
# 
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
# 
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
# 
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.

import random

def rock_paper_scissors():
  #Здесь будет игра "Камень, ножницы, бумага"
  list_strings = ['камень', 'ножницы', 'бумага']
  user_string = input('Ваш выбор: ').lower()
  cp_string = list_strings[random.randint(0, 2)]
  if user_string in list_strings:
    if user_string == cp_string:
      print(f'Ваш выбор {user_string}, мой {cp_string}, у нас НИЧЬЯ!!!')
    elif (user_string == list_strings[0] and cp_string == list_strings[1]) or (user_string == list_strings[1] and cp_string == list_strings[2]) or (user_string == list_strings[2] and cp_string == list_strings[0]):
      print(f'Ваш выбор {user_string}, мой {cp_string}, Ваша победа')
    elif (user_string == list_strings[1] and cp_string == list_strings[0]) or (user_string == list_strings[2] and cp_string == list_strings[1]) or (user_string == list_strings[0] and cp_string == list_strings[2]):
      print(f'Ваш выбор {user_string}, мой {cp_string}, Вы проиграли!!!')
  else:
    print('Вы должны вводить: камень, ножницы или бумага')
    rock_paper_scissors()

def guess_the_number():
  #Здесь будет игра "Угадай число"
  cp_num = random.randint(1, 100)
  user_num = -1
  while user_num != cp_num:
    user_num = int(input('Введите число от 1 до 100: '))
    if user_num < cp_num:
      print('Больше!!!')
    elif user_num > cp_num:
      print('Меньше!!!')
    else:
      print('УГАДАЛ!!!')

def mainMenu():
  #Здесь главное меню игры
  print()
  print('1 - «Камень, ножницы, бумага»')
  print('2 - “Угадай число”')
  print('3 - Выход')
  choice = int(input())
  if choice == 1:
    rock_paper_scissors()
    mainMenu()
  elif choice == 2:
    guess_the_number()
    mainMenu()
  elif choice == 3:
    print('До встречи!!!')

mainMenu()