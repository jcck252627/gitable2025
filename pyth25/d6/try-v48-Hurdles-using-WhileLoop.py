"""
previously

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump ():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for step in range(6):
    jump()

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json


this time we are jumping through un even hurdles so we need to use while loop


def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump ():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()



while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()



"""
