

class Thing:
    def __init__(self, name, protection, attack, hp):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.hp = hp

class Person:
    pass


class Palladin(Person):
    def __init__(self, name,  hp, base_attack, base_protect):
        super().__init__(name, hp * 2, base_attack , base_protect * 2)



class Warrior(Person)
    def __init__(self, name, hp, base_attack, base_protect)
        super.__init__(name, hp, base_attack * 2, base_protect)