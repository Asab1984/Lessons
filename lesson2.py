"""print(bool(''))
print(bool(0.0))
print(bool(None))
print(bool('Some Text'))
print(bool(1))"""

#not "Логічне заперечення"
"""previousle_fired = True
print(not previousle_fired)

previousle_fired = False
print(not previousle_fired)"""

"""time = int(input('Enter the current time in hours:')) % 24
ticket = False
money = True
luggage = False
print (time)
print((money or ticket) and not luggage and time>6)"""

# not-> and -> or

"""car_speed = int(input('enter the speed:'))
if car_speed>50:
    print('Car more 50 km/h')"""

"""car_speed = 100
if car_speed > 50 and car_speed < 150:
    print ("Car speed is between 50 km/h and 150 km/h")

car_speed = 100
if 50 < car_speed < 150 :
    print ("Car speed is between 50 km/h and 150 km/h")"""

"""a,b,c=int(input('перше ')),int(input('друге ')),int(input('третє '))
maximum = a
if maximum<b:
    maximum=b
if maximum<c:
    maximum=c
print('Max:', maximum)"""

"""if 5>4:
    print('start blok')
    print('part blok')
    print('part blok')
    print('end blok')
print('it`s not part blok')"""

"""car_speed = 110
motorcycle_speed = 100
if car_speed>motorcycle_speed:
    print('car is faster than motocycle')
elif car_speed< motorcycle_speed:
    print('motocycle faster then car')
else:
    print('equally fast')"""

"""number = int(input('Enter the answer number'))
if number == 1:
    print('A')
elif number == 2:
    print('B')
elif number == 3:
    print('C')
elif number == 4:
    print('D')
else:
    print("not result")"""

"""myname = input("Enter the login")
mypass = input('Enter the password')
if myname=='admin' and mypass == '1111':
    result = "Hi "+myname+',admin'
elif myname=='student' and mypass=='qwerty':
    result = "Hi "+myname+',student'
elif myname == "Tetiana" and mypass == 'asdqwe':
    result = "Hi " + myname
else:
    result = 'I don`t know you'
print (result)"""

"""question_1 = '2+2= '
question_2 = '3*3= '
question_3 = '5*5= '
question_4 = '2+2*2= '
answer_1 = '4'
answer_2 = '9'
answer_3 = '25'
answer_4 = '6'
result = 0
user_answer = input(question_1)
if user_answer == answer_1:
    result+=1
    print('Correct')
else:
    print('Incorrect')
user_answer = input(question_2)
if user_answer == answer_2:
    result+=1
    print('Correct')
else:
    print('Incorrect')
user_answer = input(question_3)
if user_answer == answer_3:
    result+=1
    print('Correct')
else:
    print('Incorrect')
user_answer = input(question_4)
if user_answer == answer_4:
    result+=1
    print('Correct')
else:
    print('Incorrect')
print('u have', result, 'points')"""


a = int(input('Введіть перше число '))
b = int(input('Введіть друге число '))
c = input('Введіть дію')
if c == '+':
    print(a+b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == '/':
    print(a / b)
else:
    print('Дія не передбачена')
