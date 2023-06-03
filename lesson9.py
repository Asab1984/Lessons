"""student = ['Bob', 19, 95] # name, age, score
template = "Name: {}: age: {}: scores {}"
users=['admin', 'teacher', 'meneger']

while True:
    print('1-print info')
    print('2-modify info')
    print('3 exit')
    userChoice = input('Select menu item: ')
    if userChoice=='1':
        user=input('Login: ')
        if user in users:
            print('Current information: ')
            print(template.format(student[0],student[1], student[2]))
    elif userChoice=='2':
        user = input('Login: ')
        if user in users:
            print('Current information: ')
            print(template.format(student[0], student[1], student[2]))
            userAnswer=input('Change this info y-n? ')
            if userAnswer == 'y':
                name=input('Input new name: ')
                age=input('Input new age: ')
                scores=input('Input  new score: ')
                student[0] = name
                student[1] = age
                student[2] = scores
                print(template.format(student[0], student[1], student[2]))
    elif userChoice == '3':
        print('Bye!')
        break
    else:
         print('Error: wrong menu item')"""


# help(breakpoint)

# ceil Повертає найближче ціле значення (округлення вгору)
# floor Повертає найближче ціле значення (округлення вниз)

import math
"""a = 0.23
b = 1.87
c = 3
print(math.ceil(a))
print(math.ceil(b))
print(math.ceil(c))

print(math.floor(a))
print(math.floor(b))
print(math.floor(c))

#modf - повертаэ дробову та цылу частину числа
x = 2.45
y = 1.5
print(math.modf(x))
print(math.modf(y))

# trunc отримання цілої частини числа
x = 2.45
y = 1.5
print(math.trunc(x))
print(math.trunc(y))

# abs  - повертає модуль числа з таким самим типом як і вихідне число
# fabs - повертає модуль числа з типом float

q = 2
w = -2.5
e = 4
print(math.fabs(q))
print(math.fabs(w))
print(math.fabs(e))

print(abs(q))
print(abs(w))
print(abs(e))

# factorial -
try:
    p = 4
    e = 7.4
    print(math.factorial(p))
    print(math.factorial(e))
except TypeError:
    print('Not correct item')"""

import random
# randint(a, b) - приймає лише два аргумента, з цього діапозону - випадкове число. Перше має завжди бути меньше другого

"""for i in range(3):
    print('step ', i+1)
    print(random.randint(1, 5))
    print(random.randint(-3, 20))
    print(random.randint(-10, -6))"""

# randange() - від одного до трьох аргументів
# randange(a) випадкове число від 0 до вказанного [0: a) від 0 до a-1
# randange(a, b)  - аналагічно randint, але верхня межа не входить в діапозон [a:b) від a до b-1
# randange(a, b, c )  - перші два числа є межами діапозону, третє - крок генератора (10, 18, 2) 10,12,14,16

"""for i in range(3):
    print('step ', i + 1)
    print(random.randrange(10))
    print(random.randrange(-4, 3))
    print(random.randrange(10, 20, 3))"""

# random - виклик без аргументів, випадкове число генерується в діапозоні від 0 до 1, не включаючи 1
"""for i in range(3):
    print('step ', i + 1)
    print(random.random())"""

# choice(L) - L - це послідовність або її ім'я
"""L = [1,24,'Bob',True, False, 7.9, 'hello']
for i in range(3):
    print(random.choice(L))
    print(random.choice(['red', 'blue', 'green']))"""


# menu = input('1 - Факторіал\n'
#              '2 - абсолютне значення\n'
#              '3 - згенерувати випадкове число від 1 до 100\n'
#              '4 - згенерувати випадкове число з самостійно заданого діапазону\n'
#              '5 - отримати цілу і дробову частини числа\n'
#              'oберіть дію -> ')


# if menu == '1':
#     zn = int(input('Введіть  ціле число, факторіал якого треба отримати -> '))
#     print(math.factorial(zn))
# elif menu == '2':
#     zn = float(input('Введіть число -> '))
#     print(abs(zn))
# elif menu == '3':
#     for i in range(10):
#         print(random.randint(1, 100), end =', ')
# elif menu == '4':
#     for i in range(10):
#         a = int(input('Введіть начало діапозону -> '))
#         b = int(input('Введіть кінець діапозону -> '))
#         print(random.randint(a, b))
# elif menu == '5':
#     a = float(input('Введіть число -> '))
#     print(math.modf(a))
# else:
#     print('not correct item')

"""def printMsg():
    print('Hello')
    print('Welcome')
printMsg()
print('Bye!')"""

# def printMsg1(myMsg):
#     print(myMsg)
#
# def printMsg2(myMsg1, myMsg2):
#     print(myMsg1)
#     print(myMsg2)
#
# myMsg1 = 'Hello'
# myMsg2 = 'World'
# printMsg2(myMsg1, myMsg2)

"""def calculate(a,b,c):
    print('lets calculate')
    print(a+b*c**2)

q=5
w=2
e=3
calculate(q, w, e)
calculate(q, w, 3)
calculate(5, 2, 3)"""

# def modifyName(userName):
#     newName = userName.upper()
#     return  newName
# name = input('input your name: ')
# print(modifyName(name))
# print(f'user name: {modifyName(name)}')
# a = modifyName(name)
# b = a + '. Hello user'
# print(b)

"""def calc(a,b):
    return a+b
a=float(input('input a: '))
b=float(input('input b: '))

if calc(a,b)<=0:
    y=5*a+2*b
else:
    y = 10*a - 3*b
print('y = ', y)"""

# def checkCustomer(customer, customers):
#     result = 0
#     print('Client position in the list: ')
#     for i in range(len(customers)):
#         if customers[i]==customer:
#             print(i)
#             result+=1
#     return result
#
# customerList=['Bob', 'Anna', 'Joe', 'Bob', 'Nick']
# myCustomer = input('Enter name ')
#
# if checkCustomer(myCustomer, customerList)>1:
#     print(f'customer {myCustomer}, will get a discount')

"""def modifyName2(userName):
    newName1 = userName.upper()
    newName2 = userName.lower()
    return newName1,newName2

name=input('enter your name -> ')
print(modifyName2(name))
nameUpper, nameLower = modifyName2(name)
print(nameUpper)
print(nameLower)"""

# def checkLog(userLog):
#     if userLog == 'admin':
#         return userLog.upper()
#     elif userLog == 'user':
#         return userLog.lower()
#     else:
#         return  'Wrong login'
#
# login = input('Enter your login: ')
# print(checkLog(login))

"""def meanF(*args):
    s=0
    k=0
    for i in args:
        s+=i
        k+=1
    return s/k
print('(1+5+7)/3=', meanF(1,5,7))
print('(1+5+7+4+9+12+13)/7=', meanF(1,5,7,4,9,12,13))"""

# def userGreetings(login, passw='111'):
#     if login=='admin':
#         print('Welcome, admin')
#         print(passw)
#     elif login == 'student':
#         print('Welcome, student')
#     else:
#         print('IDN who are u')
#
# userGreetings('admin')
# userGreetings('admin', 'qwerty')

def calcBMI(m,h):
    return m/(h**2)

print(calcBMI(h=1.6, m=50)) # іменовані
print(calcBMI(50, 1.6))     # позиційні





