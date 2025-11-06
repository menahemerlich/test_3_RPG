import random
from core.orc import Ork
from core.goblin import Goblin
from core.player import Player

class Game:
    def start(self):
        self.show_menu()

    def show_menu(self):
        choice = None
        while choice != "1" or choice != "2":
            print("Hello\n"
                  "What do you want to do today? \n"
                  "1. Play 2. \n"
                  "Go out")
            choice = input("your choice: ")
            if choice == "1":
                player_options = ["cure", "fighter"]
                player_choice = random.randint(0, 1)
                player = Player("Avi", player_options[player_choice])
                monster = self.choose_random_monster("Bob")
                self.battle(player, monster)
            elif choice == "2":
                break
            else:
                print("Typo error")
        return None

    @staticmethod
    def choose_random_monster(name):
        type_options = ["orc", "goblin"]
        weapon_options = ["knife", "sword", "axe"]
        type_choice = random.randint(0, 1)
        weapon_choice = random.randint(0, 2)
        if type_options[type_choice] == "orc":
            monster = Ork(name, weapon_options[weapon_choice])
        else:
            monster = Goblin(name, weapon_options[weapon_choice])
        return monster

    def battle(self, player, monster):
        for i in [player, monster]:
            dice = self.roll_dice(6)
            i.speed += dice
        if monster.speed > player.speed:
            status = monster.attack(monster, player, game1)
        else:
            status = player.attack(player, monster, game1)

        while status[1].hp > 0:
            if status[0] == player:
                status = player.attack(player, monster, game1)
            else:
                status = monster.attack(monster, player, game1)

    @staticmethod
    def roll_dice(sides):
        dice = random.randint(1, sides)
        return dice


game1 = Game()




