import random
import Player
import Weapon


class ComputerPlayer(Player.Player):
    def __init__(self):
        super().__init__("Computer")

    def choose_weapon(self):
        weapons = Weapon.Weapon.get_available_weapons()
        choice = random.randint(1, 3)
        self.weapon = weapons[choice]
        return self.weapon
