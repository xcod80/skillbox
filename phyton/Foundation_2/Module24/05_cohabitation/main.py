from random import randint

class Home:
    refrigerator = 50
    bedside = 0
class Man:
    satiety = 50
    alive = True
    def __init__(self, name='Nemo', home=Home):
        self.name = name
        self.home = home
    def action(self, choice):
        if self.satiety < 20:
            self.eat()
        elif self.home.refrigerator < 10:
            self.go_to_market()
        elif self.home.bedside < 50:
            self.work()
        elif choice == 1:
            self.work()
        elif choice == 2:
            self.eat()
        else:
            self.play()
    def eat(self):
        if self.alive and self.home.refrigerator > 0:
            self.home.refrigerator -= 1
            self.satiety += 1
            print(self.name, 'поел.')
        else:
            print(self.name, 'нет еды!.')
    def work(self):
        if self.alive:
            self.satiety -= 1
            self.home.bedside += 1
            print(self.name, 'поработал.')
        if self.satiety <= 0:
            self.alive = False
    def play(self):
        if self.alive:
            self.satiety -= 1
            print(self.name, 'поиграл.')
        if self.satiety <= 0:
            self.alive = False
    def go_to_market(self):
        if self.home.bedside > 0 and self.alive:
            self.home.bedside -= 1
            self.home.refrigerator += 1
            print(self.name, 'сходил в магазин.')
        else:
            print(self.name, 'нет денег.')

sweethome = Home()
man = Man('Артём', sweethome)
woman = Man('Алла', sweethome)
day = 1
while man.alive and woman.alive:
    man.action(randint(1, 6))
    woman.action(randint(1, 6))
    print("День", day)
    print(f'{man.name}:\tСытость:{man.satiety}')
    print(f'{woman.name}:\tСытость:{woman.satiety}')
    print(f'Денег: {sweethome.bedside}\t')
    if day == 365:
        print('Вы прожили вместе ровно 1 год!!!\nСЧАСТЛИВОГО БРАКОСОЧЕТАНИЯ!!!')
        break
    day += 1
else:
    print('Эксперимент провалился!!!! Вы не смогли прожить 1 год! :(')