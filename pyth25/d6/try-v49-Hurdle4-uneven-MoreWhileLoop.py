"""
hurdles 4



def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_or_higher ():
    turn_left()
    while wall_on_right():
        move()

    turn_right()
    move()
    turn_right()

    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump_or_higher()
    else:
        move()




    






"""