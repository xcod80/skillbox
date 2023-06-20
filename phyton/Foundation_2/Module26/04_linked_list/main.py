class Item:
    def __init__(self, data=None):
        self.__data = data
        self.__next = None

    def get_next(self):
        # Получить ссылку на следующий элемент
        return self.__next

    def set_next(self, data):
        # Установить ссылку на слудущий элемент
        self.__next = data

    def get_data(self):
        # Получить содержимое элемента
        return self.__data


class LinkedList:
    def __init__(self):
        self.__head: Item = None
        self.__cur = -1

    def __str__(self):
        outlist = list()
        tmp = self.__head
        while tmp != None:
            outlist.append(tmp.get_data())
            tmp = tmp.get_next()
        return str(outlist)
    def __iter__(self):
        return self
    def __next__(self):
        if self.__cur +1 == self.count():
            raise StopIteration
        self.__cur += 1
        return self.get(self.__cur)
    def push(self, data):
        if self.__head == None:
            self.__head = Item(data)
        else:
            tmp = Item(data)
            tmp.set_next(self.__head)
            self.__head = tmp

    def pop(self):
        if self.__head == None:
            return Item(None)
        else:
            tmp = self.__head
            self.__head = self.__head.get_next()
            return tmp

    def is_empty(self):
        if self.__head == None:
            return True
        else:
            return False

    def count(self):
        # глубина стека
        tmp = self.__head
        cnt = 0
        while not tmp == None:
            tmp = tmp.get_next()
            cnt += 1
        return cnt

    def get(self, cnt):
        # Получить данные по номеру
        # счет идет от верхнего эдемента (0) в глубину (item_cnt)
        if cnt > self.count() -1:
            raise IndexError
        tmp = self.__head
        for item_cnt in range(cnt):
            tmp = tmp.get_next()
        return tmp.get_data()

    def append(self, data):
        if self.__head == None:
            self.push(data)
            return
        tmp = self.__head
        while tmp.get_next() != None:
            tmp = tmp.get_next()
        tmp.set_next(Item(data))

    def remove(self, cnt):
        if cnt > self.count() -1:
            raise IndexError
        tmp = None
        for index in range(self.count()):
            if index != cnt:
                if tmp == None:
                    tmp = self.__head
                    safehead = tmp
                else:
                    tmp.set_next(Item(self.get(index)))
                    tmp = tmp.get_next()
                    self.__head = self.__head.get_next()
        self.__head = safehead

my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(2)
print('Новый список:', my_list)

print('Итератор:')
for item in my_list:
    print(item)