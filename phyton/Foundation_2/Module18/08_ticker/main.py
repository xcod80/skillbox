first_string, second_string = input("Первая строка: "), input("Вторая строка: ")

if first_string == second_string[second_string.find(first_string[0]):] + second_string[:second_string.find(first_string[0])]:
    print("Первая строка получается из второй со сдвигом", second_string.find(first_string[0]))
else:
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")