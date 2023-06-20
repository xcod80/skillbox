nature = {None:0, 'Вода':1, 'Воздух':2, 'Огонь':3, 'Земля':4}
class Element:
    elements = [[None, 'Вода', 'Воздух', 'Огонь', 'Земля'],
                ['Вода', None, 'Шторм', 'Пар', 'Грязь'],
                ['Воздух', 'Шторм', None, 'Молния', 'Пыль'],
                ['Огонь', 'Пар', 'Молния', None, 'Лава'],
                ['Земля', 'Грязь', 'Пыль', 'Лава', None]]
    def __init__(self, element = None):
        self.element = element
    def __add__(self, other):
        add_elem = self.elements[self.elements[0].index(other.element)][self.elements[0].index(self.element)]
        return Element(add_elem)
    def print(self):
        print(self.element)
    def value(self):
        return self.element

water = Element('Вода')
air = Element('Воздух')

storm = water + air

storm.print()