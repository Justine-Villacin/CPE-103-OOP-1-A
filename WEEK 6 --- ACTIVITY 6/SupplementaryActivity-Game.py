import random
import time


# Base class for all characters
class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.wins = 0

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 2, self.attack_power + 2)
        opponent.hp -= max(0, damage)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        time.sleep(1)

    def is_alive(self):
        return self.hp > 0


# Subclasses for different roles
class Novice(Character):
    def __init__(self, name):
        super().__init__(name, 20, 5)


class Swordsman(Character):
    def __init__(self, name):
        super().__init__(name, 30, 7)


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, 25, 8)


class Magician(Character):
    def __init__(self, name):
        super().__init__(name, 22, 10)


class Boss(Character):
    def __init__(self):
        super().__init__("Monster", 40, 6)


# Function to handle a match
def battle(player1, player2):
    print(f"\nBattle starts between {player1.name} and {player2.name}!\n")
    players = [player1, player2]
    random.shuffle(players)  # Randomizing turns

    while player1.is_alive() and player2.is_alive():
        attacker, defender = players[0], players[1]
        attacker.attack(defender)
        print(f"{defender.name} has {defender.hp} HP left.\n")
        if not defender.is_alive():
            print(f"{attacker.name} wins the match!\n")
            attacker.wins += 1
            return attacker
        players.reverse()  # Swap turns


# Function to start the game
def start_game():
    while True:
        mode = input("Choose mode: 1 for Single Player, 2 for Player vs Player, 0 to Exit: ")
        if mode == "0":
            print("Exiting game...")
            break
        elif mode == "1":
            single_player_mode()
        elif mode == "2":
            player_vs_player_mode()
        else:
            print("Invalid choice, try again.")


# Single Player Mode
def single_player_mode():
    name = input("Enter your name: ")
    player = Novice(name)
    wins_needed = 2

    while True:
        print(f"\nStarting match {player.wins + 1}!")
        opponent = Boss()
        winner = battle(player, opponent)

        if winner == player:
            if player.wins == wins_needed:
                print("\nCongratulations! You can now select a new role:")
                player = choose_role(name)
        else:
            print("You lost! Try again.")

        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            break


# Player vs Player Mode
def player_vs_player_mode():
    name1 = input("Enter Player 1 name: ")
    name2 = input("Enter Player 2 name: ")
    player1 = choose_role(name1)
    player2 = choose_role(name2)

    while True:
        print(f"\nStarting match between {player1.name} and {player2.name}!")
        battle(player1, player2)

        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            break


# Role selection function
def choose_role(name):
    roles = {"1": Swordsman, "2": Archer, "3": Magician}
    while True:
        choice = input("Choose a role - 1: Swordsman, 2: Archer, 3: Magician: ")
        if choice in roles:
            return roles[choice](name)
        print("Invalid choice, try again.")


if __name__ == "__main__":
    start_game()
