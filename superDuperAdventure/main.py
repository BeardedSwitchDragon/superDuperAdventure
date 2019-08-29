from play import *
from clothing import *
from street1 import *
Player = Player(54)


def run():
    start = input2("Super Duper Adventure: Press Enter To Continue or Press S to check stats")
    start2 = input2("You are in your nice cozy cabin. You took a morning nap on the rocking chair in front of the crackling fireplace.")
    start3 = input2("Learn more about your house? [Y/N]")
    if yesOrNo(start3):
        Player.update()
        start5 = input2(
        """\n The walls are made of polished pine tree logs,
         and the television is a bit old.
          \n Downstairs there is a dank and dusty cellar that you never use because
          you love the tasty and tangy taste of store-bought orange juice. \n
          Your sentient pet Black Hole, named 'Water-bottle and a 1/2 Snr' \n was incredibly exhausted
          from watching the television for too long.  \n The floor is made of an unknown
          substance, but it is really creaky. \n All was cold except for that comforting, fading
          heat of the dying fire.""")
    start4 = input2("There's a closet, do you want to check or change your outfit [Y/N]?")
    if yesOrNo(start2):
        closet()
        Player.update()
    start5 = input2("Prepare some food?")
    if yesOrNo(start3):
        pantry()
        Player.update()
    start6 = input2("Go outside?")

def yesOrNo(q):
    if  q == "N" or q == "no" or q == "No":
        return False
    if q == "Y" or q == "yes" or q == "Yes":
        return True
#input2 replaces input so it checks everytime if you want to check stats
def input2(enter_input):
    entered = input(enter_input)

    if entered == "s" or entered == "S":
        displayStats()
        entered = input(enter_input)
    return entered

def displayStats():

        print("Hunger: " + str(Player.hunger))
        print("Health: " + str(Player.health))
        print("Warmth: " + str(Player.warmth))
        print("Snazz: " + str(Player.snazz))
        print("Hat:" + Player.clothing["Hat"])
        print("Shirt" + Player.clothing["Shirt"])
        print("Pants" + Player.clothing["Pants"])
        print("Shoes" + player.clothing["Shoes"])

def closet():
    closet1 = input2("Your items are: ")
    for key in Player.clothing:
        print(key, "          ", Player.clothing[key])
def pantry():
    Player.foodItems["Pantry"] = {False: 0, "Cereal": 12, "Milk": 8, "Egg": 21, "Salad Mix": 17, "Oatmeal": 50, "armadillo": 100, "ibygu54534weAAw@1aaaa??": 999, "faeces": 300}
    pantry1 = input2("Your food choices are: ")
    #False is to determine whether you can access it outside
    print()
    for key in Player.foodItems["Pantry"]:
        if key != False:
            print(key)
            print()
    pantry2 = input2("So what will it be? ")

    for key in Player.foodItems["Pantry"]:
        if key == pantry2 or key.lower() == pantry2:
            print(key + " it is!")
            Player.health += Player.foodItems["Pantry"][key]/(50 + Player.foodItems["Pantry"][key])
            Player.health -= Player.foodItems["Pantry"][key]/(50 + Player.foodItems["Pantry"][key])
            print("ate the " + key)
            Player.foodItems["Pantry"].pop(key, None)
            #Removes food item from dictionary




run()
