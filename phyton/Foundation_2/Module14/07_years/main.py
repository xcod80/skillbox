# TODO здесь писать код

while True:
    start_year, end_year = input("Введите первый год:"), input("Введите второй год:")
    if start_year.isdigit() and end_year.isdigit() and len(start_year) == 4 and len(end_year) == 4:
        if int(start_year) > int(end_year):
            start_year, end_year = end_year, start_year
        break
    else:
        print("Введите целые четырёхзначные числа!\n")

for year in range(int(start_year), int(end_year)+1):
    for i in range(0, 10):
        if str(year).count(str(i)) ==3:
            print(str(year))
