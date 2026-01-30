import WeaponMode


class Weapon:
    def __init__(self, weapon_mode):
        self.weapon_mode = weapon_mode
        self.name = weapon_mode.name.capitalize()

    def beats(self, other):
        winning_combinations = {
            WeaponMode.WeaponMode.ROCK: WeaponMode.WeaponMode.SCISSORS,
            WeaponMode.WeaponMode.PAPER: WeaponMode.WeaponMode.ROCK,
            WeaponMode.WeaponMode.SCISSORS: WeaponMode.WeaponMode.PAPER
        }
        return winning_combinations[self.weapon_mode] == other.weapon_mode

    @staticmethod
    def get_available_weapons():
        return {
            1: Rock(),
            2: Paper(),
            3: Scissors()
        }

    @staticmethod
    def print_weapon_options():
        print("1) Rock")
        print("2) Paper")
        print("3) Scissors")

    def __str__(self):
        return self.name


class Rock(Weapon):
    def __init__(self):
        super().__init__(WeaponMode.WeaponMode.ROCK)


class Paper(Weapon):
    def __init__(self):
        super().__init__(WeaponMode.WeaponMode.PAPER)


class Scissors(Weapon):
    def __init__(self):
        super().__init__(WeaponMode.WeaponMode.SCISSORS)
