def how_are_you(func):
    def wrapper(*args, **kwargs):
        input("Как дела? ")
        print("А у меня не очень! Ладно, держи свою функцию.")
        result = func(*args, **kwargs)
        return result
    return wrapper
@how_are_you
def test():
    print('<Тут что-то происходит...>')
@how_are_you
def gett(data:str):
    print(data)
    return (data[::-1])

test()

print(gett(input("Введите текст: ")))