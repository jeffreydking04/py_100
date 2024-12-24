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

# I could do stuff like this all day.
