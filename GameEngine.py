import Weapon
import WeaponMode


class GameEngine:
    player_weapon: Weapon.Weapon
    computer_weapon: Weapon.Weapon

    def __init__(self, player_weapon: Weapon.Weapon, computer_weapon: Weapon.Weapon):
        self.player_weapon = player_weapon
        self.computer_weapon = computer_weapon

    def decide_winner(self) -> str:
        if self.player_weapon.weapon_mode == self.computer_weapon.weapon_mode:
            return "tie"
        winning = {
            WeaponMode.WeaponMode.ROCK: WeaponMode.WeaponMode.SCISSORS,
            WeaponMode.WeaponMode.PAPER: WeaponMode.WeaponMode.ROCK,
            WeaponMode.WeaponMode.SCISSORS: WeaponMode.WeaponMode.PAPER,
        }
        if winning[self.player_weapon.weapon_mode] == self.computer_weapon.weapon_mode:
            return "player"
        return "computer"
