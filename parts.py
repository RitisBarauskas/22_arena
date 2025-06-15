THINGS = [
"Меч 'Секретный ингредиент – боль'",
"Щит для прятания от мамы",
"Меч 'Ой, кажется, я промахнулся'",
"Щит 'Защита от дурацких решений'",
]


class Thing:
    def __init__(self, name, protection, attack, hp):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.hp = hp


class Person:
    def __init__(self, name, hit_points, base_attack, protection_percentage):
        self.name = name
        self.hit_points = hit_points
        self.attack_damage = base_attack
        self.base_protection = protection_percentage
        self.things = []


    def set_things(self, things: Thing):
        self.things = things.copy()
        self.current_hit_points = self.hit_points + sum(thing.hp for thing in self.things)


    def get_final_protection(self):
        """
        Вычисляет общий процент защиты.
        """
        return self.base_protection + sum(t.protection for t in self.things)

    def subtract_life(self, damage):
        """
        Вычитает урон из текущего количества жизней.
        """
        self.hit_points -= (damage - damage * self.get_final_protection())
        return self.hit_points


class Paladin(Person):
    def __init__(self, name,  hp, base_attack, base_protect):
        super().__init__(name, hp * 2, base_attack, base_protect * 2)


class Warrior(Person):
    def __init__(self, name, hp, base_attack, base_protect):
        super().__init__(name, hp, base_attack * 2, base_protect)
