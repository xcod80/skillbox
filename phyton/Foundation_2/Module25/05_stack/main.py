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


class Stack:
    def __init__(self):
        self.__head: Item = None

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

    def get_itembycount(self, cnt):
        # Получить данные по номеру
        # счет идет от верхнего эдемента (0) в глубину (item_cnt)
        tmp = self.__head
        item_cnt = 0
        while item_cnt != cnt:
            tmp = tmp.get_next()
            item_cnt += 1
        return tmp


class TaskManager:
    def __init__(self):
        self.__tasks = Stack()

    def __str__(self):
        ret_string = ''
        for i in range(self.__min_id(), self.__max_id() + 1):
            tmp = self.get_taskbyid(i)
            if tmp != None:
                ret_string += str(tmp.get_data()[0]) + ' ' + str(tmp.get_data()[1]) + '\n'
        return ret_string

    def new_task(self, name: str, id: int):
        # Добавляет задачу, если задача с таким id уже была,
        # объединит задачу с существующей.
        tmp = self.get_taskbyid(id)
        if tmp != None:
            name = str(tmp.get_data()[1]) + '; ' + name
            self.del_task(id)
        self.__tasks.push((id, name))

    def del_task(self, id):
        # Удалить задачу по id
        tmp_stack = Stack()
        tmp = self.__tasks.pop()
        while tmp.get_data() != None:
            if tmp.get_data()[0] != id:
                tmp_stack.push((tmp.get_data()[0], tmp.get_data()[1]))
            tmp = self.__tasks.pop()
        self.__tasks = tmp_stack

    def __max_id(self):
        item_id = 0
        for i in range(0, self.__tasks.count()):
            tmp = self.__tasks.get_itembycount(i)
            if item_id < tmp.get_data()[0]:
                item_id = tmp.get_data()[0]
        return item_id

    def __min_id(self):
        item_id = 0
        for i in range(0, self.__tasks.count()):
            tmp = self.__tasks.get_itembycount(i)
            if item_id > tmp.get_data()[0]:
                item_id = tmp.get_data()[0]
        return item_id

    def get_taskbyid(self, id=0):
        # Получить задачу по id
        for i in range(0, self.__tasks.count()):
            tmp = self.__tasks.get_itembycount(i)
            if tmp.get_data()[0] == id:
                return tmp
        else:
            return None


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
manager.del_task(2)
print(manager)
