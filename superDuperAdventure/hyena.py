from play import *
class Hyena(Player):
    def __init__(self, heat):
        super().__init__(heat)
        self.clothing = {}
        self.warmth = heat
