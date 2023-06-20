class Square:
    def __init__(self, N):
        self.__max = N
        self.__cur = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.__cur += 1
        if self.__cur <= self.__max:
            return self.__cur ** 2
        raise StopIteration

def square(N):
    for i in range(1, N+1):
        yield i ** 2
while True:
    try:
        N = int(input('Введите целое число: '))
    except Exception:
        print('Ошибка ввода!!! Повторите ввод.')
    else:
        break


for res in Square(N):
    print(res)

for res in square(N):
    print(res)

square_list = (num ** 2 for num in [i for i in range(1, N+1)])
for res in square_list:
    print(res)
