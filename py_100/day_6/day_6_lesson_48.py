# Lesson 48: Hurdles challenge using While loops

# Working in Reeborg's World again

# Hurdle 3:  Unknown spaces between hurdles, unknown goal

# dummy think which is a Reeborg function to set the amount of time between steps.
def think(num):
    pass

think(0)

def move():
    pass

def turn_left():
    pass

def at_goal():
    pass

# Reeborg defined function, is the space the robot is facing free to move()d into
def front_is_clear():
    pass

def turn_right():
    for x in range(0,3):
        turn_left()
                
def move_and_turn_right():
    move()
    turn_right()
        
def move_and_turn_left():
    move()
    turn_left()
    
def jump_hurdle():    
    turn_left()
    move_and_turn_right()
    move_and_turn_right()
    move_and_turn_left()
    
while not at_goal():
    while front_is_clear() and not at_goal():
        move()
    if not at_goal():
        jump_hurdle()

# better version from Instructor Yu:

def wall_in_front():
    pass

while not at_goal():
    if wall_in_front():
        jump_hurdle()
    else:
        move()
