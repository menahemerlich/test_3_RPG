import random

class Player:
    def __init__(self, name, profession):
        self.name = name
        self.hp = 50
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.armor_rating = random.randint(5, 15)
        self.profession = profession
        if self.profession == "cure":
            self.hp += 10
        elif self.profession == "fighter":
            self.power += 2

    def speak(self):
        print(self.name)

    @staticmethod
    def attack(attacker, attacked, game_instance):
        print("Player's turn.")
        dice = game_instance.roll_dice(20) + attacker.speed
        if dice > attacked.armor_rating:
            damage = game_instance.roll_dice(6) + attacker.power
            attacked.hp -= damage
        attacker, attacked = attacked, attacker
        return attacker, attacked


