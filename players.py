
class Person:
    """Базовый класс персонажа"""
    def __init__(self, name):
        self.things = []
        self.name = name
        self.attack = 50
        self.defence = 50
        self.hp = 100
        self.hp_total = self.hp
        self.attack_total = self.attack
        self.defence_total = self.defence

    def set_things(self, thing):
        self.things.append(thing)

    def set_total_skills(self):
        for thing in self.things:
            self.hp_total += self.hp * thing.lives
            self.attack_total += self.attack * thing.attack
            self.defence_total += self.defence * thing.protection

    def get_defence(self, player1):
        damage = player1.attack_total - self.defence_total
        if damage >= 0:
            self.hp_total -= damage


class Paladin(Person):
    def __init__(self, name):
        super().__init__(name)
        self.defence *= 2
        self.hp *= 2


class Warrior(Person):
    def __init__(self, name):
        super().__init__(name)
        self.attack *= 2
