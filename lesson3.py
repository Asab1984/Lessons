"""print('Hello', end='-->' )
print('World')

print('Hello', 'World', 'Hi')
print('Hello', 'World', 'Hi', sep='-->')

print('''
1   ^
2  |  |
3   <>
''')

number1 = input('num 1 = ')
print(type(number1))"""

"""number1 = 25
number2 = 0

try:
    print(number1 / number2)
except:
    print('ZeroDivisionError')

try:
      x=5
      y='3'
      print(x**y)
except:
    print('Error!')"""


#error='error'
"""try:
    print('start code')
    print(error)
    print(15/0)
    print('no errors')
except (NameError, ZeroDivisionError)as error:
    print(error)
"""
#print('\n\tcode after capsule')
"""except NameError:
    print('We have an NameError')

except ZeroDivisionError:
    print('We have an NameError')"""

"""try:
    try:
        print('start code')
        print(10/0)
        print(error_1)
        print('no errors')
    except NameError as error:
        print(error)
except ZeroDivisionError as error:
    print(error)"""

"""try:
    print('Hello')
except:
    print('! problems')
else:
    print('no problems')
finally:
    print('Finally code')

import  tkinter as tk
root = tk.Tk()
root.title('First Application')
label = tk.Label(root, text='Text', fg='blue', bg='yellow', font=('Arial', 20, 'bold italic'))
label.pack()
root.mainloop()"""

"""try:
    try:
        apples=int(input('Enter the amount of apples you have: '))
        if apples < 0:
            raise Exception
        print('You have ', apples, 'apples')
    except Exception:
        print('You can`t have ', apples, ' appels')
    except NameError:
        print('bad idea')
except:
    print('error')"""

"""try:
    raise Exception
except ValueError:
    print('Imporoper value was obtained')
except Exception:
    print('.... Something went wrong')"""


"""try:
    f=open('Some_text.txt')
except ZeroDivisionError:
    print('Error 1')
except:
    print('Errors ...')"""

day = 4
month = 'april'
year = 2023
print('Today is', day, month, year, ".")
#f-strings
print(f'Today is {day} {month} {year}.')
print(f'Today is {day:8} {month:12} {year:10}.')
print(f'Today is {day:^8} {month:>12} {year:<10}.')
print(f'Today is {day:_^8} {month:*^12} {year:#^10}.')

#format()
print('Today is {} {} {}.'.format(year,month,day))
print('Today is {:#^10.3f} {:*^12} {:_^8}.'.format(year,month,day))
print('Today is {year1:#^10.3f} {month1:*^12} {day1:_^8}.'.format(year1=2022,month1='marth',day1=3))