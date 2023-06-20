class Property:
    def __init__(self, worth):
        self.worth = worth
    def SalaryCalc(self):
        return self.worth * 0.13

class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)
    def SalaryCalc(self):
        return self.worth / 1000

class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)
    def SalaryCalc(self):
        return self.worth / 200

class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)
    def SalaryCalc(self):
        return self.worth / 500

while True:
    try:
        totalmoney = float(input('Введите количество денег на счете: '))
        apartment = Apartment(float(input('Введите стоимость квартиры: ')))
        car = Car(float(input('Введите стоимость машины: ')))
        countryhouse = CountryHouse(float(input('Введите стоимость дачи: ')))
    except ValueError:
        print('Необходимо вводить только числа.\nПопробуйте заново.\n')
    else:
        break
totalmoney -= (apartment.SalaryCalc() + car.SalaryCalc() + countryhouse.SalaryCalc())
print('Налог на квартиру составит:', round(apartment.SalaryCalc(),2))
print('Налог на машину составит:', round(car.SalaryCalc(),2))
print('Налог на дачу составит', round(countryhouse.SalaryCalc(),2))
if totalmoney < 0:
    print('Для уплаты налогов Вам нехватает:', -round(totalmoney,2))
else:
    print('После уплаты налогов останется:', round(totalmoney,2))
