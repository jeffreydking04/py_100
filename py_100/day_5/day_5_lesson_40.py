# Lesson 40: for loops and the range() function

for number in range(1, 10):
    print(number)

# range() is start inclusive, end exclusive so range(0, 2) is 0, 1

# range() does not produce a List

print(range(1, 11)) # prints 'range(1, 11)'

gauss = 0

for n in range(1,101):
    gauss += n

print(gauss)

