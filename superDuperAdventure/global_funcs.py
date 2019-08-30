def input2(enter_input, player):
    entered = input(enter_input)

    if entered == "s" or entered == "S":
        displayStats(player)
        entered = input(enter_input)
    return entered
def displayStats(Player):

        print("Hunger: " + str(Player.hunger))
        print("Health: " + str(Player.health))
        print("Warmth: " + str(Player.warmth))
        print("Snazz: " + str(Player.snazz))
        print("Hat:  " + Player.clothing["Hat"])
        print("Shirt:  " + Player.clothing["Shirt"])
        print("Pants:  " + Player.clothing["Pants"])
        print("Shoes:  " + Player.clothing["Shoes"])
def yesOrNo(q):
    if  q == "N" or q == "no" or q == "No":
        return False
    if q == "Y" or q == "yes" or q == "Yes":
        return True
