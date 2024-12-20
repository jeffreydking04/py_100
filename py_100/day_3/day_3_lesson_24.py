# Nested if statement and elif

print('Welcome to the rollercoaster')

height = int(input('What is your height in cm?\n'))

if height >= 120:
    print('Yes, you may!')
    age = int(input('What is your age?\n'))
    if age > 18:
        print('Please pay $12.')
    elif age > 11:
        print('Please pay $7.')
    else:
        print('Please pay $5.')
else:
    print('Sorry you have to grow taller bfore you can ride.')
