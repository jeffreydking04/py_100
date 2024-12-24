# Lesson 45: Jumping Hurdles in Reeborg's World 


# Code from Reeborg's World interface:

# turn_left() and move() are defined in Reeborg's World.  I am giving dummy versions here so no errors.

def move():
    pass

def turn_left():
    pass

def turn_right():
    for x in range(0,3):
        turn_left()

def move_and_turn_right_twice():
    for x in range (0,2):
        move()
        turn_right()
        
def move_and_turn_left():
    move()
    turn_left()
    
def jump_hurdle():
    move_and_turn_left()
    move_and_turn_right_twice()
    move_and_turn_left()
    
for x in range(0,6):
    jump_hurdle()
