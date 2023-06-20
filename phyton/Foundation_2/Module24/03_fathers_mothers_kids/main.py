from random import randint
class Child:
    child_psy = {0:'Спокойный', 1:'Испуган', 2:'Нервный', 3:'Плачет'}
    child_hung = {0:'Голодный', 1:'Сытый', 2:'Хочет пить'}
    def set_states(self):
        self.state_hung = randint(0, 2)
        if self.state_hung == 0:
            self.state_psy = 3
        elif self.state_hung == 2:
            self.state_psy = 2
        else:
            self.state_psy = randint(0, 1)
    def __init__(self, name='none', age=0):
        self.name = name
        self.age = age
        self.set_states()

class Parent:
    childs = list()
    def __init__(self, name='Nemo', age=16):
        self.name = name
        self.age = age
        return
    def add_child(self, child):
        if isinstance(child, Child):
            if child.age+16 <= self.age:
                self.childs.append(child)
                return True
            else:
                return False
        else:
            return False
    def calm(self):
        for child in self.childs:
            print(f'Ребенок {child.name} {child.child_psy[child.state_psy]}')
            if child.state_psy > 0:
                child.state_psy -= 1
            print(f'Ребенок {child.name} {child.child_psy[child.state_psy]}')
    def feed(self):
        for child in self.childs:
            print(f'Ребенок {child.name} {child.child_hung[child.state_hung]}')
            if child.state_hung == 0:
                child.state_hung += 1
            elif child.state_hung == 2:
                child.state_hung -= 1
            print(f'Ребенок {child.name} {child.child_hung[child.state_hung]}')

parent = Parent('Васян', 30)
parent.add_child(Child('Васятка', 4))
parent.add_child(Child('Анютка', 10))
while True:
    for ch in parent.childs:
        ch.set_states()
    parent.feed()
    parent.calm()
    choice = input('Введите 1 для выхода')
    if choice == '1':
        exit()