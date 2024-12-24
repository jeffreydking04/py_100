# Lesson 49: Jumping over Hurdles with variable heights

# Working in Reeborg's World again

# Hurdle 3:  Unknown spaces between hurdles, unknown goal, unknown height

# Reeborg functions dummied here:
def move():
    pass
def turn_left():
    pass
def wall_on_right():
    pass
def front_is_clear():
    pass
def at_goal():
    pass
def wall_in_front():
    pass

def turn_right():
    for x in range(0,3):
        turn_left()
    
def jump_hurdle():    
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
        jump_hurdle()
    else:
        move()
