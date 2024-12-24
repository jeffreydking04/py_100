# Lesson 47: While loops

# Working in Reeborg's World again
# Reworking first hurdle problem

def move():
    pass

def turn_left():
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
    
def jump_hurdle(number_of_hurdles):
    iteration = number_of_hurdles
    while iteration > 0:    
        move_and_turn_left()
        move_and_turn_right()
        move_and_turn_right()
        move_and_turn_left()
        iteration -= 1
    
jump_hurdle(6)

# Next Hurdle Problem (with unknown goal)

def at_goal():
    pass

def jump():    
    move_and_turn_left()
    move_and_turn_right()
    move_and_turn_right()
    move_and_turn_left()
    
while not at_goal():
    jump()

# Another little gem: When writing while loops, print your condition
# Example (commented out for obvious reasons)

# while True:
#     print(True)
