# m=lambda a,d:a/d
# print(m(4,2))
'''mult=lambda a,b,c:a*b*c
print(mult(5,2,9))
result=mult(5,2,9)
print(result)

def multdef(a,b,c):
    return a*b*c
print(multdef(5,2,9))
result=multdef(5,2,9)
print(result)'''
# import math
# abs=lambda a,b:math.sqrt(a*a + b*b)
# result=abs(3,4)
#
# def ads_def(a,b):
#     return math.sqrt(a*a + b*b)
# resultdef=ads_def(3,4)
#
# print(result)
# print(resultdef)

'''discr=lambda a,b,c:b*b -4*a*c
print(discr(3,4,5))

def discr_def(a,b,c):
    return b*b -4*a*c
print(discr_def(3,4,5))'''

# import random
# spysok=[lambda : random.random(),
#         lambda : random.random(),
#         lambda : random.random()]
#
# for i in spysok:
#     print(i())

'''cort=(lambda x:x*2,
      lambda x:x*3,
      lambda x:x*5)
for i in cort:
    print(i(2))

for i in cort:
    print(i('qwerty'))
'''
# slovnyk={1:(lambda: print('Понеділок')), 2:(lambda: print("Вівторок")),
#          3:(lambda: print('Середа')), 4:(lambda: print('Четвер')),
#          5:(lambda: print('Пятниця'))}
#
# answer=int(input('Число від 1 до 5'))
# try:
#     slovnyk[answer]()
# except KeyError:
#     print('incorrect value')
'''import math

area={'circle':(lambda r:math.pi*r*r),
      'rectangle':(lambda a,b:a*b),
      'trapezoid':(lambda a,b,h:(a+b)*h/2.0)}

answer=input('Enter figure')
if answer.lower()=='circle':
      answer1=int(input('enter r'))
      print('Площа круга = ', area['circle'](answer1))
elif answer.lower()=='rectangle':
      answer1=int(input('enter a'))
      answer2=int(input('enter b'))
      print('Площа трикутника = ', area['rectangle'](answer1, answer2))
elif answer.lower()=='trapezoid':
      answer1 = int(input('enter a'))
      answer2 = int(input('enter b'))
      answer3 = int(input('enter h'))
      print('Площа трапеції = ', area['trapezoid'](answer1, answer2, answer3))'''
# summ=lambda a=1,b=2,c=3:a+b+c
# print(summ())
# print(summ(5))
# print(summ(10,20))
# print(summ(10,20,25))

'''def func(a=2,b=3):
      return a+4+b
print(func())
print(func(4))
print(func(5,8))'''
# import random
# def randomNumber():
#       n=random.random()
#       res=lambda : int(n*100)
#       return res()
#
# print(randomNumber())
'''max=(lambda a,b: a if a>b else b)
print(max(23,70))
print(max(21,4))'''
# minimum =(lambda a,b,c:a if(a<=b)and(b<=c) else (b if (b<=a)and(b<=c) else c))
# print(minimum(21,34,56))
# print(minimum(34,21,56))
# print(minimum(3,2,1))
'''def mnoj_dva(x):
    return x*2

spysok =[6,1,2,3,4,5,7,8]

spysok2=list(map(mnoj_dva, spysok))
print(spysok2)

spysok3=list(map((lambda x:x*2), spysok))
print(spysok3)
'''
# cort =(2.88,-5.97,9.78)
#
# cort2=tuple(map((lambda x:int(x)), cort))
# print(cort2)
'''cort=('qwerty','hello','abc','qwe','jkl','word')
cort2=tuple(filter((lambda x:len(x)==3), cort))
print(cort2)'''
# spysok = [3, 5, 2, 12, 15, 25, 57, 150, 3, 1, 9, 60, 56, 45, 98]
# spysok2=list(filter((lambda x:(x<=10)or(x>=60)or(x==25)), spysok))
# print(spysok2)
#
# def vid_10_do_30(x):
#     return (x>=10) and (x<=30)
# spysok3=list(filter(vid_10_do_30, spysok))
# print(spysok3)
'''import re
spysok_1='Bob Anna Alice Alex Gena Bob'
spysok_2='adc qwe rty gfd'
vyraz=re.compile('Bob') #compile-створення рядку, якйи ми шукаємо
vyraz_2=re.compile('qwe')
match1=vyraz.search(spysok_1)# search позиція першого входження елементу
print(match1)
match2=vyraz.search(spysok_2)# search Якщо елемент не було знайдено - None
print(match2)
match3=vyraz.finditer(spysok_1)# finditer Знайти усі збіги і їх позиції
for i in match3:
    print(f'match_1 - {i}')

match4=vyraz.findall(spysok_1) #findall знайти усі збіги і помістити їх у список
print(match4)
print(len(match4))

spysok_2='adc qwe rty gfd'
poshuk=re.compile('rty')
new=poshuk.sub('HelloWorld', spysok_2) #sub-заміна патерну на інше значення
print(new)'''
# import re
# rechennya='По всім питання писати на пошту qwerty-1@gmail.com, або на newadress@ukr.net, або на itstep@outlook.com'
# emails=re.findall(r'[\w]+@[\w]',rechennya)
# for i in emails:
#     print(i)
#\w цифри, букви, _
#^-початок рядка
#$-рядок закінчився

import tkinter as tk
import re
loggin_pattern=re.compile(r"^\w{3,20}@[a-z]{2,10}\.[a-z]{2,6}$")
password_pattern=re.compile(r"^\w{8,16}$")
root=tk.Tk()
root.geometry('400x250+700+500')
root.resizable(False,False)
def logining():
    pass
login_label=tk.Label(root, text='Login', font=('Arial',14), padx=50)
password_label=tk.Label(root,text='Password', font=('Arial',14), padx=50)


root.grid_columnconfigure(0, minsize=150)

login_label.grid(column=0, row=0)
root.mainloop()


