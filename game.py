import random 

from classes import Thing, Paladin, Warrior


def generate_things(count):
    names = ['Меч', 'Щит', 'Кольцо', 'Шапка', 'Плащ']
    things = []
    for _ in range(count):
        name = random.choice(names)
        hp = random.randint(1, 17)
        protection = random.randint(1, 10) / 100
        attack =random.randint(1, 15)

        things.append(Thing(name=name,
                            protection=protection,
                            attack=attack,
                            hp=hp))

    return sorted(things, key=lambda x: x.protection)
