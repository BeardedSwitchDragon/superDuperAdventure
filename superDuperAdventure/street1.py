
from global_funcs import *
def Street1run(Player):
    streetin1 = input2("You go outside, there's a cold fog. The city was quiet.", Player)
    streetin2 = input2("A blurry figure approaches from the right", Player)
    streetin3 = input2("It seems the figure is a dog", Player)
    streetin4 = input2("Closer...", Player)
    streetin4 = input2("Closer...", Player)
    streetin5 = input2("Closer...", Player)
    streetin6 = input2("It  now seems like the figure is a hyena.", Player)
    streetin7 = input2(" 'Do you have food? Hee hee' asks the hyena, invite the Hyena in? [Y/N]", Player)
    if yesOrNo(streetin7):
        streetin8 = input2("'Thhh-anksss... he he' says the Hyena, you invite him in.", Player)
        streetin9 = input2("You show him the food options", Player)

        for key in Player.foodItems["Pantry"]:
            if key != False:
                print(key + "\n")



    #return Player
