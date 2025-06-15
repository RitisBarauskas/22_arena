class Arena:
    """Класс для создания объекта арены сражений"""

    def __init__(self, capacity=10):
        self.capacity = capacity
        self.players = []

    def add_player(self, player):
        if len(self.players) < self.capacity:
            self.players.append(player)
