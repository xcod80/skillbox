import re
auto_nums = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

auto_personaly = re.findall(r'\b\w\d{3}\w{2}\d{2,3}\b', auto_nums)
auto_taxi = re.findall(r'\b\w{2}\d{5,6}\b', auto_nums)
print('Список номеров частных автомобилей:', auto_personaly)
print('Список номеров такси:', auto_taxi)