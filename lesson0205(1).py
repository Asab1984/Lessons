# student = ['Bob', 19, 95] #name, age, score
# template="Name: {}; age: {}; scores {}"
# users=['admin','teacher','manager']
#
# while True:
#     print('1-print info')
#     print('2-modify info')
#     print('3-exit')
#     userChoice = input('Select menu item: ')
#     if userChoice=='1':
#         user=input('Login:')
#         if user in users:
#             print('Current information:')
#             print(template.format(student[0],
#                                   student[1],
#                                   student[2]))
#     elif userChoice=='2':
#             user = input('Login:')
#             if user in users:
#                 print('Current information:')
#                 print(template.format(student[0],
#                                       student[1],
#                                       student[2]))
#                 userAnsw=input('Change this info y-n?')
#                 if userAnsw=='y':
#                     name=input('Input new name:')
#                     age=input('Input new age:')
#                     scores=input('Input new score:')
#                     student[0]=name
#                     student[1]=age
#                     student[2]=scores
#                     print(template.format(student[0],
#                                           student[1],
#                                           student[2]))
#     elif userChoice=='3':
#         print('Bye!')
#         break
#     else:
#         print('Error: wrong menu item')
'''help(breakpoint)'''

# #math.ім'я функції(...)
# #ceil Повертає найближче ціле значення, (округлення вгору)
# #floor Повертає найближче ціле значення, (округлення вниз)
# import math
# a=0.23
# b=1.87
# c=3
# print(math.ceil(a))
# print(math.ceil(b))
# print(math.ceil(c))
#
# print(math.floor(a))
# print(math.floor(b))
# print(math.floor(c))
#
# #modf()-повертає дробову та цілу частину числа
# x=2.0
# y=1.5
# print(math.modf(x))
# print(math.modf(y))
# #trunc() - отримання цілої частини числа
# x=2.45
# y=1.5
# print(math.trunc(x))
# print(math.trunc(y))
# #abs - повертає модуль числа з таким самим типом, як і вихідне число
# #fabs -  повертає модуль числа з типом float
#
# q=-2
# w=-2.5
# e=4
# print(math.fabs(q))
# print(math.fabs(w))
# print(math.fabs(e))
#
# print(abs(q))
# print(abs(w))
# print(abs(e))
#
# #factorial-факторіал 4!=4*3*2*1=24 ЗАВЖДИ, якщо число не ціле - VALUE ERROR(TYPE ERROR)
# p = 4
# e = 7.4
# try:
#     print(math.factorial(p))
#     print(math.factorial(e))
# except ValueError:
#     print('Not correct item')


#randint(a,b) - приймає лише два аргумет, з цього діапазону-випадкове число. Перше має
#завжди бути менше другого
"""
import random
for i in range(3):
    print('step ', i+1)
    print(random.randint(1,5))
    print(random.randint(-3,20))
    print(random.randint(-10,-6))"""
# randrange() - від одного до трьох аргументів
# randrange(a) - випадкове число від 0 до вказаного [0;a) від 0 до а-1
# randrange(a,b) - аналогічно randint, але верхня межа не входить в діапазон [a;b) від a до b-1
# randrange(a,b,c) - перші два числа є межами діапазону, третє-крок генератора. (10, 18, 2) 10, 12, 14,16
'''import random
for i in range(3):
    print('step ', i+1)
    print(random.randrange(10))
    print(random.randrange(-4,3))
    print(random.randrange(10,20, 3)) #10 13 16 19'''
#random - виклик без аргументів, випадкове число генерується в діпазоні від 0 до 1, але не включаючи 1
"""import random
for i in range(3):
    print('step ', i+1)
    print(random.random())"""
#choice(L) - L-це послідовність або її ім'я. Функція для отримання випадкового елементу з послідовності
import random
L=[1,24,'Bob', True, False, 7.9, 'hello']
for i in range(3):
    print(random.choice(L))
    print(random.choice(['red','blue','green','white']))