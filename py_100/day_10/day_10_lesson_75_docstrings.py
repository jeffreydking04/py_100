# Day 10 Lesson 74: Multiple Return Statements

import os

def clear_screen():
    os.system('clear')

clear_screen()

def format_name(first_name, last_name):
    '''Take a first and last name and format it to return title case version of the name.'''
    return f'{first_name} {last_name}'.title()

format_name('jeff', 'king')
