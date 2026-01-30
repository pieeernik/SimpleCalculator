import GameEngine
import HumanPlayer
import ComputerPlayer


def main():
    player = HumanPlayer.HumanPlayer()
    computer = ComputerPlayer.ComputerPlayer()
    player_wins = 0
    computer_wins = 0
    ties = 0

    while True:
        print("Rock Paper Scissors")
        print("Score - You:", player_wins, "| Computer:", computer_wins, "| Ties:", ties)

        player_weapon = player.choose_weapon()
        computer_weapon = computer.choose_weapon()

        print(player, "chose:", player_weapon)
        print(computer, "chose:", computer_weapon)

        engine = GameEngine.GameEngine(player_weapon, computer_weapon)
        result = engine.decide_winner()

        if result == "player":
            player_wins += 1
        elif result == "computer":
            computer_wins += 1
        else:
            ties += 1

        winner = "You" if result == "player" else "Computer" if result == "computer" else "Tie"
        print("Winner:", winner)


if __name__ == "__main__":
    main()
