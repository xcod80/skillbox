import time

def dalay(func):
    def wrapper(*args, **kwargs):
        start_t = time.time()
        while time.time() - start_t < 10:
            pass
        result = func(*args, **kwargs)
        return result
    return wrapper
@dalay
def square(num):
    return num ** 2

print(square(1234567890))