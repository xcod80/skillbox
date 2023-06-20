import functools
import time
import datetime
def timestamp(cls, func, timeformat):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        timef = timeformat
        print(f' - Запускается {cls.__name__}.{func.__name__} Дата и время запуска: {datetime.datetime.now().strftime(timef)}')
        startt = time.time()
        result = func(*args, **kwargs)
        endt = time.time()
        print(f' - завершение {cls.__name__}.{func.__name__}, время работы = {endt - startt} сек.')
        return result
    return wrapper


def log_methods(timeformat:str = None):
    def wrapper(cls):
        timef = timeformat
        for sym in timef:
            if sym.isalpha():
                timef = timef.replace(sym, '%' + sym)
        for method in dir(cls):
            if not method.startswith('__'):
                cur_method = getattr(cls, method)
                dec_method = timestamp(cls, cur_method, timef)
                setattr(cls, method, dec_method)
        return cls
    return wrapper

@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result

@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")
    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result




my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()