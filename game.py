import random

from classes import Thing, Paladin, Warrior


def generate_things(count):
    names = ['Меч', 'Щит', 'Кольцо', 'Шапка', 'Плащ']
    things = []
    for _ in range(count):
        name = random.choice(names)
        hp = random.randint(1, 17)
        protection = random.randint(1, 10) / 100
        attack = random.randint(1, 15)

        things.append(Thing(name=name,
                            protection=protection,
                            attack=attack,
                            hp=hp))

    return sorted(things, key=lambda x: x.protection)


def generate_persons(count=10):
    names = [
        "Ардрик", "Бальтазар", "Вейн", "Гаррик", "Дартмунд",
        "Эдрик", "Фарран", "Горин", "Хельга", "Ингвар",
        "Йормунд", "Креллис", "Лира", "Морван", "Нейла",
        "Орик", "Петра", "Квандлин", "Роланд", "Сигрид"]
    persons = []
    for _ in range(count):
        name = random.choice(names)
        names.remove(name)
        hp = random.randint(100, 150)
        protection = random.randint(1, 25) / 100
        attack = random.randint(1, 20)
        if (random.randint(1, 10) % 2 == 0):
            persons.append(Paladin(name=name,
                                   hp=hp,
                                   base_attack=attack,
                                   base_protect=protection))
        else:
            persons.append(Warrior(name=name,
                                   hp=hp,
                                   base_attack=attack,
                                   base_protect=protection))
    return persons


def get_things(persons):
    for person in persons:
        person.set_things(generate_things(random.randint(1, 4)))
    return persons



def get_winner(persons):
    round_num = 1
    while len(persons) > 1:
        print(f"\n=== Раунд {round_num} ===")
        print(f"Осталось бойцов: {len(persons)}")
        person1, person2 = random.sample(persons, 2)
        while True:
            person2.subtract_life(person1.attack())
            if person2.hit_points > 0:
                person1.subtract_life(person2.attack())
            if person1.hit_points <= 0:
                print(f'Персонаж {person1.name} был убит {person2.name}! И выбыл с арены')
                persons.remove(person1)
                break
            elif person2.hit_points <= 0:
                print(f'Персонаж {person2.name} был убит {person1.name}! И выбыл с арены')
                persons.remove(person2)
                break
        round_num += 1
    return persons[0]


persons = get_things(generate_persons())
winner = get_winner(persons)
print(f'Победитель турнира {winner.name}')
