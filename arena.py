from random import choices


class Arena:
    """Класс для создания объекта арены сражений"""

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.players = []

    def add_player(self, player):
        if len(self.players) < self.capacity:
            self.players.append(player)

    def choice_two_players(self):
        self.player1, self.player2 = choices(self.players, k=2)

    def make_move(self):
        self.player1