import Player
import Weapon


class HumanPlayer(Player.Player):
    def __init__(self):
        super().__init__("You")

    def choose_weapon(self):
        Weapon.Weapon.print_weapon_options()
        while True:
            try:
                choice = int(input("Enter your choice (1-3): "))
                if choice in (1, 2, 3):
                    weapons = Weapon.Weapon.get_available_weapons()
                    self.weapon = weapons[choice]
                    return self.weapon
                print("Invalid choice. Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")
