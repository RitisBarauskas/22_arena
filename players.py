
class Person:
    """Базовый класс персонажа"""
    def __init__(self, name):
        self.things = []
        self.name = name
        self.atack = 50
        self.defence = 50
        self.hp = 100
        self.hp_total = self.hp
        self.atack_total = self.atack
        self.defence_total = self.defence

    def set_things(things):
        self.things = things

    def set_total_skills(self):
        for thing in self.things:
            self.hp_total = self.hp
            self.atack_total = self.atack
            self.defence_total = self.defence


class Paladin(Person):
    def __init__(self, name):
        super().__init__(name)
        self.defence *= 2


class Warrior(Person):
    def __init__(self, name):
        super().__init__(name)
        self.atack *= 2
