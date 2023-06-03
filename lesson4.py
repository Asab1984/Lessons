"""number = int(input('Enter the number (1-9)-> '))
while number < 10:
    print('number = ', number)
    number += 1.5

print ('Cycle is over')
print('________________')
number = int(input('Enter the number (1-9)-> '))
while True:
    print('number = ', number)
    number += 1.5
    if number >= 10:
        break
    str = input('Do you want to continue? - ')
    if str == 'no' or str == 'N':
        break"""

import random
"""#from random import randint
print('Game - Guess the number')
bot_num = random.randint(1, 10)
#bot_num = randint(1, 10)
num_2 = 0
while True:
    num_2 += 1
    user_num = int(input('Enter the number (1-10) -> '))
    if user_num > bot_num:
        print('Your number is more than the bot`s')
    elif user_num < bot_num:
        print('Your number is less than the bot`s')
    elif user_num == bot_num:
        print('Guessed right')
        print('Game over!')
        print(f'Hidden number - {bot_num}')
        print(f"You guessed right in {num_2} attempts")
        break
    if num_2 > 2:
        print('Loser!')
        break"""

"""bot_num = random.randint(1, 10)
user_num = 0
num_2 = 0
while True:
    while bot_num != user_num:
        user_num = int(input('Enter the number (1-10) -> '))
        if user_num > bot_num:
            print('Your number is more than the bot`s')
        elif user_num < bot_num:
            print('Your number is less than the bot`s')
    print('Guessed right')
    print('Game over!')
    print(f'Hidden number - {bot_num}')
    print(f"You guessed right in {num_2} attempts")
    str = input ('Do you want to continue? Y/N ->')
    if str == 'Y' or str == 'y':
        bot_num = random.randint(1,10)
    else:
        break
print('OK')"""

"""number = input('Enter an integer -> ')
while type(number) != int:
    try:
        number = int(number)
    except ValueError:
        print('wrong number entered')
        number = input('Enter an integer -> ')
print('OK')"""

#print('5 + 5**2 = ', eval('5+5**2'))

# for cycle
"""x=5
for i in 2,3,4:
    x+=i
    print(f'{i} --> x = {x}')

for i in range(5):
    x += i
    print(f'{i} --> x = {x}')

for i in range(1, 11):
    print('i - ', i)

for i in range(1, 11, 3):
    print('i - ', i)"""

"""for i in range(1, 11, 3):
    print('i - ', i, end=' ')
    if i % 2 == 0:
        print ('Парне \n')
    else:
        print('Непарне \n')"""

"""str = 'stringS'
#print(len(str))
#print(str[0])
#print(str[-7])
for i in range(len(str)):   #for i in range(7):
    print(str[i])

lst = [27, 'mama', ['papa', 56], 67]
for i in lst:
    print(i)
print(lst[2][0])"""

"""str = input('Enter some string - ')
for i in str:
    print(str)
line = input('Enter some string - ')
for c in line:
    print(c)"""

"""str = 'mamapapa'
print(str[0:4])
print(str[:4:2])

line=input('enter som text - ')
for c in line[::2]:
    print(c)"""


"""for i in range(1,10):
    for j in range(1,10):
        print(f'i-{i} j-{j} i*j={i * j}', end='\t')
    print('\n')"""

floor = 1
energy =30
while floor != 5:
    print('floor before - ', floor)
    step = 0
    while step != 20:
        step += 1
        energy -= 1
        if energy == 0:
            print('Відпочинь!')
            energy += 30
    floor += 1
    print('floor after - ', floor)
print('floor = 5')



