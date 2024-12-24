# Lesson 50: Project: Escape the maze

# Working in Reeborg's World again

# Mazes

# Reeborg functions dummied here:
def move():
    pass
def turn_left():
    pass
def front_is_clear():
    pass
def at_goal():
    pass
def right_is_clear():
    pass
def wall_in_front():
    pass

def turn_right():
    for x in range(0,3):
        turn_left()
        
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

# That doesn't work for edge cases

number_of_times_moved_right_in_succession = 0

while not at_goal():
    if number_of_times_moved_right_in_succession == 4 and front_is_clear():
        number_of_times_moved_right_in_succession = 0
        move()
    if right_is_clear():
        number_of_times_moved_right_in_succession += 1
        for x in range(0, 3):
            turn_left()
        move()
    elif front_is_clear():
        move()
        number_of_times_moved_right_in_succession = 0
    else:
        turn_left()
        number_of_times_moved_right_in_succession = 0

# even better:

def turn_right():
    for x in range(0, 3):
            turn_left()
            
while wall_in_front():
    turn_right()
    
while front_is_clear() and right_is_clear():
    move()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

# but even better to ensure the starting spot has a wall on the right (because once that happens, the robot will always follow the wall on right)
# This is basically Instructor Yu's solution: move forward if you can; if you can't you are facing a wall; turn left so wall is on right

def turn_right():
    for x in range(0, 3):
            turn_left()
            
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

# I could do stuff like this all day.
