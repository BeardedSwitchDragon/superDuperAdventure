from play import *
class Clothing():
    def __init__(self):
        self.snazz = 0
        #Snazz is a feature that fluctuates the way prople interact with you
        #With no clothing your snazz is 0
        self.selection = {"Hat": "None", "Shirt": "None", "Pants": "None", "Shoes": "None"}
        self.clothingHeat = 3

class Basic(Clothing):
    def __init__(self):
        super().__init__()
        #self.selection = {"Basic Bowler Hat": 13, "Basic Black Sweater": 6, "Basic Baggy Jeans": 3, "Basic Red Polo Shirt": 9, "Neon Sneakers": 7}
        self.snazz = 8
        self.selection["Hat"] = "Basic Bowler Hat"
        self.selection["Shirt"] = "Basic Taco suit"
        self.selection["Pants"] = "Basic Baggy Jeans"
        self.selection["Shoes"] = "Basic Neon Sneakers"
        self.selection["Hat2"] = "Basic Orange Cap"
        self.selection["Shirt2"] = "Basic Plain White Shirt"
        self.selection["Pants2"] = "Basic Track-pants"
        self.selection["Shoes2"] = "Basic Black Leather Shoes"

class Nude(Clothing):
    def __init__(self):
        super().__init__()
        self.snazz = 0
