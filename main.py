import time
from random import choice, randint

from players import Warrior, Paladin
from arena import Arena
from things import Thing

PLAYERS_COUNT = 10
PLAYERS_NAMES = (f'Player{i}'for i in range(1, 21))
THINGS_NAMES = (f'Thing{i}'for i in range(1, 21))


if __name__ == '__main__':
    arena = Arena()
    for i in range(PLAYERS_COUNT):
        name = choice(PLAYERS_NAMES)
        player = choice(Warrior, Paladin)(name)
        for j in randint(1, 5):
            player.set_things(Thing(choice(THINGS_NAMES)))
        arena.add_player(player)
        time.sleep(1)
        print(f'На арену вышел боец {name} с характеристиками...')
    while True:
