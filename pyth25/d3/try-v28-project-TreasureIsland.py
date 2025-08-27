
"""
use ASCII art LATER!!!

*****************************************
"""
print("*****************************************************************")
print("Welcome to Teasure Island, Your mission is to find the treasure")
print("*****************************************************************")

first_q = input("This is your crossroad ...Left or Right ?   ").lower()

if first_q == "left":
    print("You have reached an ocean")
    second_q = input("Now what you do? ...Swim or Wait ?  ").lower()
    if second_q == "wait":
        print("Your wait was worth it, now time to catch a boat ....")
        third_q = input("The boat has taken you to an island with 3 doors ... which one would you choose ? blue,yellow or red? ").lower()
        if third_q == "yellow":
            print("You have found GOLD !! ... alots of GOLD !!!")
        elif third_q == "blue":
            print("Unluckily, you were eaten by a beast jump out of the blue door !!! ... GANE OVER")
        elif third_q_q == "red":
            print("It's HOT in here, you were consumed by region of fire !!! ... GAME OVER")
        else:
            print("You have made a wrong choice ... GAME OVER prematurely")


else:
   print("You have choosen the wrong side ... GAME OVER !!")

