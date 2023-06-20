def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print('Запуск №', wrapper.count)
        result = func(*args, **kwargs)
        return result
    wrapper.count = 0
    return wrapper

@counter
def test():
    print('тестики крестики')

@counter
def test2():
    print('ёлики болики')


test()
test2()
test()
test()
test2()