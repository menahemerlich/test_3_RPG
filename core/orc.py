import random

class Ork:
    def __init__(self, name, weapon):
        self.name = name
        self.hp = 50
        self.type = "orc"
        self.speed = random.randint(0, 5)
        self.power = random.randint(10, 15)
        self.armor_rating = random.randint(2, 8)
        self.weapon = weapon

    def speak(self):
        print(f"{self.type} {self.name}")

    def attack(self, attacker, attacked, game_instance):
        print("The monster's turn.")
        dice = game_instance.roll_dice(20) + attacker.speed
        if dice > attacked.armor_rating:
            damage = game_instance.roll_dice(6) + attacker.power
            if self.weapon == "knife":
                damage = damage * 0.5
            elif self.weapon == "sword":
                damage = damage
            elif self.weapon == "axe":
                damage = damage * 1.5
            attacked.hp -= damage
        print(attacker.hp)
        attacker, attacked = attacked, attacker
        return attacker, attacked
