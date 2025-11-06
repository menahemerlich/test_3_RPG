from core.orc import Ork
import random

class Goblin(Ork):
    def __init__(self, name, weapon):
        super().__init__(name, weapon)
        self.hp = 20
        self.type = "goblin"
        self.speed = random.randint(5, 10)
        self.power = random.randint(5, 10)
        self.armor_rating = 1
