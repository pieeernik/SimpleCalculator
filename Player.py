class Player:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def choose_weapon(self):
        pass

    def __str__(self):
        return self.name
