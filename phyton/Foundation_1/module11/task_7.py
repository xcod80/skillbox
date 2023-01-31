print('Задача 7. Ход конём')


# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
# 
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

while True:
  try:
    print('Введите местоположение коня:')
    horse_x = float(input())
    horse_y = float(input())
    print('Введите местоположение точки на доске:')
    dot_x = float(input())
    dot_y = float(input())
  except Exception:
    print('Ошибка ввода!')
  else:
    if horse_x >= 0.9 or horse_x < 0 or horse_y >= 0.9 or horse_y < 0 or dot_x >= 0.9 or dot_x < 0 or dot_y >= 0.9 or dot_y < 0:
      print('Ошибка ввода!')
    else:
      break

horse_x = int(horse_x * 10)
horse_y = int(horse_y * 10)
dot_x = int(dot_x * 10)
dot_y = int(dot_y * 10)

if (abs(horse_x - dot_x) == 2 and abs(horse_y - dot_y) == 1) or (abs(horse_x - dot_x) == 1 and abs(horse_y - dot_y) == 2):
  print('Да, конь может ходить в эту точку.')
else:
  print('Увы, конь не может ходить в эту точку.')
  