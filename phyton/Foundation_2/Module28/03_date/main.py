class Date:
    @classmethod
    def from_string(cls, date_string:str = '01-01-1970') -> str:
        datenums =  date_string.split('-')
        return 'День:{}\t\t Месяц:{}\t\tГод:{}'.format(datenums[0],datenums[1],datenums[2])
    @classmethod
    def is_date_valid(cls, date_string:str = '01-01-1970') -> bool:
        datenums = [int(num) for num in date_string.split('-')]
        if datenums[1] <= 12 and datenums[1] >= 1:#Проверка корретности месяца
            #Если месяц корректен, проверка корректности дня
            if datenums[1] % 2 == 0 and datenums[1] != 2 and datenums[0] >= 1 and datenums[0] <= 30:
                return True
            elif datenums[1] % 2 != 0 and datenums[1] != 2 and datenums[0] >= 1 and datenums[0] <= 31:
                return True
            elif datenums[1] == 2:
                #Вычисляем "високостность" года
                if ((datenums[2] % 4 == 0 and datenums[2] % 100 != 0 and datenums[2] % 400 != 0) or\
                    (datenums[2] % 4 == 0 and datenums[2] % 100 == 0 and datenums[2] % 400 == 0))\
                        and (datenums[0] >= 1 and datenums[0] <= 29):
                    return True
                elif (datenums[0] >= 1 and datenums[0] <= 28):
                    return True
        #дата неверная
        return False
date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))