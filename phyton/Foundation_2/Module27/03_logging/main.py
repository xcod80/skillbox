import datetime

def logging(func):
    def wrapper (*args, **kwargs):
        print(func.__name__)
        print(func.__doc__)
        try:
            result = func(*args, **kwargs)
        except Exception as error:
            with open('function_errors.log', 'a') as log_file:
                log_file.write('{}\n'.format(datetime.datetime.now()))
                log_file.write('{}\n'.format(func.__name__))
                log_file.write('{}\n'.format(error))
        else:
            return result
    return wrapper
@logging
def test(data):
    """
    Тестовая функция.
    :param data:
    :return:
    """
    print(str(data))
    2/0
@logging
def test2(data):
    """
    Тестовая функция #2.
    :param data:
    :return:
    """
    print(int(data))

test('eee')
test2('rfg')