# This is lesson 17 from Henrick Johansson's Master Pandas and Python for Data Handling

# Python While Loop

# Essential for Machine Learning and Artificial Intelligence and useful in Data Handling

loop_counter = 0 # This integer variable keeps track of the number of repetitions or iterations of the while loop
while loop_counter < 10:
    loop_counter = loop_counter + 1
    print(loop_counter)

print('This is the final value of the loop_counter Integer variable: ' + str(loop_counter))

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# This is the final value of the loop_counter Integer variable: 1

 # While loops, infinite while loops, and break statements...
 # While a while loop is a great tool for keeping a program running indefinitely, 'forever-loops' may also lock a program in
 # Execution mode.  One way to handle this is to insert break statements.
 # This While-loop creates a possible 'infinity-loop' without our 'break-exits from the loop'.
loop_counter_2 = 10
while loop_counter_2 > 5:
    loop_counter_2 = loop_counter_2 + 1
    print(loop_counter_2)
    if loop_counter_2 == 20:
        break

print('This is the final value of the loop_counter_2 Integer variable: ' + str(loop_counter_2))

# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# This is the final value of the loop_counter_2 Integer variable: 20

# An algorithmic way to use the While-loop with Python lists
list_tested = []
list_untested = ['cat', 'dog', 'horse', 'bull', 'cow']

while len(list_untested) > 0:
    print('Testiing a ' + str(list_untested[0]))
    list_tested.append(list_untested.pop(0))

print('All these animals have been tested: ')
print(*list_tested, sep=', ')

# Testiing a cat
# Testiing a dog
# Testiing a horse
# Testiing a bull
# Testiing a cow
# All these animals have been tested: 
# cat, dog, horse, bull, cow
