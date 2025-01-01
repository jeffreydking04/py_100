# Day 8 Lesson 69: Nesting Lists and Dictionaries

capitals = {
    'France': 'Paris',
    'Germany': 'Berlin',
}

# Nested List in Dictionary

travel_log = {
    'France': ['Paris', 'Lille', 'Dijon'],
    'Germany': ['Stuttgart', 'Berlin'],
}

print(travel_log['France'][1]) # Lille

nested_list = ['A', 'B', ['C', 'D']]

print(nested_list[2][1]) # D

travel_log_too = {
    'France': {
        'total_visits': 8,
        'cities_visited': ['Paris', 'Lille', 'Dijon']
    },
    'Germany': {
        'total_visits': 5,
        'cities_visited': ['Stuttgart', 'Berlin'],
    }
}

print(travel_log_too['Germany']['cities_visited'][0]) # Stuttgart


