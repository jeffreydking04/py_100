# Day 3 Project Working File: Treasure Island

print('Welcome to Treasure Island')

print('Your mission is to find the treasure.')

selected_direction = input('Would you like to go left or right?\n')

if selected_direction.lower() == 'right':
    print('Game Over.')
else:
    selected_travel_option = input('You come to a lake. Would you like to swim or wait for a boat?\n')
    if selected_travel_option.lower() == 'swim':
        print('Game Over.')
    else: 
        selected_door_color = input('You have come to a building with three doors colored red, yellow, and blue.  Which door would you like to open?\n')
        if selected_door_color.lower() == 'yellow':
            print('You Win!')
        else:
            print('Game Over.')
