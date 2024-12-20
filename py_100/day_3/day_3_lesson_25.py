# Multiple if Statements in Succession

height = int(input('What is your height in cm?\n'))
bill = 0

if height >= 120:
    print('Yes, you may!')
    age = int(input('What is your age?\n'))
    if age > 18:
        print('Adult tickets are $12.')
        bill = 12
    elif age > 11:
        print('Youth tickets are $7.')
        bill = 7
    else:
        print('Child tickets are $5.')
        bill = 5

    desires_picture = input('Would you like a picture?\n')
    if desires_picture == 'yes':
        bill += 3

    print(f'Please pay ${bill}.')
else:
    print('Sorry you have to grow taller bfore you can ride.')
