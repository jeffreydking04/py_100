# IndexError and Working with Nested Lists

states_of_america_in_order_of_entrance = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(len(states_of_america_in_order_of_entrance))

print(states_of_america_in_order_of_entrance[49]) # the 50th state admitted; colonizatian for the win

# IndexError: list index out of range

# print(states_of_america_in_order_of_entrance[50]) # commented out so the rest of the code will run

number_of_states = len(states_of_america_in_order_of_entrance)

print(states_of_america_in_order_of_entrance[number_of_states - 1])

# this kinda sucks; you have to keep using - 1 for indexing

# nested lists

dirty_dozen = [
    [
        'Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears'
    ],
    [
        'Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes'
    ]
]

# A nested list that made me a better typist!

print(dirty_dozen)
