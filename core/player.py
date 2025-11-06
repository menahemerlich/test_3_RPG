import random

class Player:
    def __init__(self, name, profession):
        self.name = name
        self.hp = 50
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.armor_rating = random.randint(5, 15)
        self.profession = profession

    def type_profession(self):
        if self.profession == "cure":
            self.hp += 10
        elif self.profession == "fighter":
            self.power += 2

    def speak(self):
        print(self.name)

    def attack(self):
        pass


