

class Player():
    self.__init__(Player)
    self.money = 0
    self.weapons = {}
    self.clothing = {"Basic": "Bowler Hat", "Basic": "Black Comfy Sweater", "Basic": "Baggy Jeans", "Basic": "Neon Red & Blue Sneakers"}
    self.items = {}
    self.health = 50
    self.hunger = 0
    self.moves = 0

    def increaseMoney(self, increase):
        self.money += increase
        self.update()
    def increaseHunger(self):
        self.hunger += 1
        if self.moves %= 25:
            self.hunger += 1
        if self.hunger >= 10:
            self.health -= 3*(self.hunger)

    def update(self):
        self.increaseHunger()
        self.moves += 1
