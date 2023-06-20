from random import randint
class Warrior:
    health = 100
    dead = False
    def __init__(self, name):
        self.name = name
    def hit(self, point=0):
        if self.health > point:
            print(f'Полуен удар в {point} очков здоровья!!!')
            self.health -= point
        else:
            self.health = 0
            self.dead = True
            print(f'Полуен удар в {point} очков здоровья!!!')
            print('Наступила смерть', self.name)

warrior_1, warrior_2 = Warrior('Вася'), Warrior('Петя')
while not warrior_1.dead and not warrior_2.dead:
    queue = randint(1,2)
    if queue == 1:
        print(f'Воин {warrior_1.name} наносит удар Воину {warrior_2.name}')
        warrior_2.hit(randint(0, 10))
    elif queue == 2:
        print(f'Воин {warrior_2.name} наносит удар Воину {warrior_1.name}')
        warrior_1.hit(randint(0,10))
