from play import *
from clothing import *
from street1 import *
from hyena import *
from global_funcs import *
Player = Player(54)
Hyena = Hyena(56)

def run():
    start = input2("Super Duper Adventure: Press Enter To Continue or Press S to check stats", Player)
    start2 = input2("You are in your nice cozy cabin. You took a morning nap on the rocking chair in front of the crackling fireplace.", Player)
    start3 = input2("Learn more about your house? [Y/N]", Player)
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
          heat of the dying fire.""", Player)
    start5 = input2("There's a closet, do you want to check or change your outfit [Y/N]?", Player)
    if yesOrNo(start5):
        closet()
        Player.update()
    start6 = input2("Prepare some food?", Player)
    if yesOrNo(start6):
        pantry()
        Player.update()
    start7 = input2("You Go outside", Player)
    Street1run(Player)
    hyenaInHome()




#input2 replaces input so it checks everytime if you want to check stats


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

    pantry1 = input2("Your food choices are: ", Player)
    #False is to determine whether you can access it outside
    print()
    for key in Player.foodItems["Pantry"]:
        if key != False:
            print(key)
            print()
    pantry2 = input2("So what will it be? ", Player)

    for key in Player.foodItems["Pantry"]:
        if key != False:
            if key == pantry2 or key.lower() == pantry2:
                print(key + " it is!")
                Player.health += Player.foodItems["Pantry"][key]/(50 + Player.foodItems["Pantry"][key])
                Player.hunger -= Player.foodItems["Pantry"][key]/(50 + Player.foodItems["Pantry"][key])
                print("ate the " + key)
                Player.foodItems["Pantry"].pop(key, None)
                break
            #Removes food item from dictionary
            #break is used since error is raised when you pop the item and still iterate through it

def hyenaInHome():
    hihin1 = input2("'I'll take whattttever you have. he he.' What will you give the hyena?", Player)
    for key in Player.foodItems["Pantry"]:
        if key != False:
            if key == hihin1 or key.lower() == hihin1:
                print(key + " it is!")
                Hyena.health += Player.foodItems["Pantry"][key]/(50 + Player.foodItems["Pantry"][key])
                Hyena.hunger -= Player.foodItems["Pantry"][key]/(50 + Player.foodItems["Pantry"][key])
                print("Hyena ate the " + key)
                Player.foodItems["Pantry"].pop(key, None)
        
                break



run()
