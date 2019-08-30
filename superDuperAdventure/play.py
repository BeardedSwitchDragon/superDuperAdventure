from clothing import *
from global_funcs import *

class Player():
    def __init__(self, clothingHeat):
        self.money = 0
        self.weapons = {}
        self.clotheType = Basic()
        self.clothing = { "Hat": self.clotheType.selection["Hat"], "Shirt": self.clotheType.selection["Shirt"], "Pants": self.clotheType.selection["Pants"], "Shoes": self.clotheType.selection["Shoes"]}
        self.foodItems = {}
        self.foodItems["Pantry"] = {False: 0, "Cereal": 12, "Milk": 8, "Egg": 21, "Salad Mix": 17, "Oatmeal": 50, "armadillo": 100, "ibygu54534weAAw@1aaaa??": 999, "faeces": 300}
        self.health = 50
        self.hunger = 0
        self.warmth = 50
        self.snazz = self.clotheType.snazz
        self.moves = 0

    def increaseMoney(self, increase):
        self.money += increase
        self.update()
    def increaseHunger(self):
        if self.hunger < 100:
            self.hunger += 1
        if self.moves % 25 == 0:
            self.hunger += 1
        if self.hunger >= 10:
            self.health -= 3*(self.hunger)

    def update(self):
        self.increaseHunger()
        self.moves += 1
        if self.warmth >= 110 or self.warmth <= 25:
            self.health -= (self.warmth*self.warmth)/20

    def changeClothing(self, index, key, value):
        pass
