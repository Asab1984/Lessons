"""myStr = 'hello'
print(id(myStr))
print(type(myStr))
print(myStr)

zminna_ryadok = '''Hello1
Hello2
Hello3'''
print(zminna_ryadok)

a='Python'
print(a[0])
print(a[1])
print(a[-1])
print(a[len(a)-1])"""

"""a='Hello'
b='World'
print(a+b)
print(a*5)"""

"""a = "Lexus isn't releasing any details About the new LM but the adjacent Teaser image Lexus suggests it’s a second-generation model"
print(a.capitalize()) #Перший символ - верхній регістр, інші - ніжній
print(a.lower())  #усі символи нижній регістр
print(a.upper())  #усі символи у верхній регістр
print(a.title())  #Перші літери - верхній пегістр, усі інші - нижній
print(a.swapcase()) #змінює регістр на протилежний

print(a.count('Lexus'))         # кількість входжень фрагмента до рядка
print(a.count('Lexus',20,65))   # кількість входжень фрагмента до рядка с 20 до 65 символу
print(a.count('Lexus',20))      # кількість входжень фрагмента до рядка с 20 до кінця

print(a.find('any'))      # індекс першого входження елемента
print(a.find('Lexus', 20))
print(a.find('Lexus', 20, 65))

print(a.index('any')) # індекс першого входження елемента, якщо нема ValueError
try:
    print(a.index('Lexus', 20, 65))
except ValueError:
    print('Фрагмент не знайдено')
finally:
    print('Дякуємо, що скористалися нашим пошуком')

print(a.rfind('About')) # індекс останнього входження
print(a.rfind('any', 20, 65))


print(a.rindex('any')) # індекс останнього входження елемента, якщо нема ValueError
try:
    print(a.index('Lexus', 20, 65))
except ValueError:
    print('Фрагмент не знайдено')
finally:
    print('Дякуємо, що скористалися нашим пошуком')

b = input('Enter the word -> ')
print('Це слово зустрічається ', a.count(b), 'разів')"""

"""a = "Lexus isn't releasing any details About the new LM but the adjacent Teaser image Lexus suggests it’s a second-generation model."
print(a.startswith('l')) # чи починається рядок з заданого фрагменту
print(a.startswith('L'))
print(a.startswith('Lexus'))
print(a.startswith('l', 50))

print(a.endswith('.'))      # чи закінчується рядок на заданий фрагмент
print(a.endswith('s', 0, 5))"""

"""stroka = 'Python2023'
print(stroka.isalnum()) # ПЕРЕВІРЯЄ ЧИ РЯДОК СКЛАДАЄТЬСЯ ЛИШЕ З ЛІТЕР І ЧИСЕЛ
print(stroka.isalpha()) # ПЕРЕВІРЯЄ ЧИ РЯДОК СКЛАДАЄТЬСЯ ЛИШЕ З  ЛІТЕР
print(stroka.isdigit()) # ПЕРЕВІРЯЄ ЧИ РЯДОК СКЛАДАЄТЬСЯ ЛИШЕ З  ЧИСЕЛ"""

"""a = input('enter 1 number -> ')
b = input('enter 2 number -> ')
if a.isdigit()==True and b.isdigit()==True:
    c=int(a)+int(b)
    print(c)
else:
    print('некоректне значення')"""

"""str = 'hello'
print(str.islower())    # перевіряє чи всі елементи рядка в нижньому регістрі
print(str.istitle())    # перевіряє чи кожне слово рядка починається з великої літери
print(str.isupper())    # перевіряє чи всі елементи рядка в верхноьму регістрі

str1 = '\n\t\n     \n'  # лише пробыловы символи - пробіл, \n, \t
print(str1.isspace())

str = 'Pyt\thon'
print(str.center(30))
print(str.center(30,'*'))
print(str.center(50,'~'))
print(str.expandtabs(tabsize=8)) # задаємо скількі пробілів в \t
print(str.ljust(30))
print(str.ljust(30, '~'))
print(str.rjust(30))
print(str.rjust(30, '-'))"""

"""str = 'Python-cool!'
print(str[1:3]+str[5:7])
print(str[-5:-2])
print(str[-5:11])
print(str[7:])
print(str[:6])

str1='0123456789'
print(str1[2:8:2])
print(str1[9:2:-2])
print(str1[::-1])
print(str1[5::2])
print(str1[-1::-2])
print(str1[:len(str1):3])"""

# a = r'\n-newline'
# print(a)
# b = R'\t\tAddition+\n'
# print(b)
# c=r'\'
# print(c)
# d=r'abc\\\'

# day = 11
# month = 'Квітень'
# print('Today is {}.{}'.format(day, month))
# print('Today {day}.{month}.{year}'.format(month=month, day=11, year=2023))

# name='Olha'
# year = 2023
# print(f'Hello, {name}')
# print(f'Hello {name*2}')
# print(f'Hello {name:~^30}. Now is {year}')
# print(f'Hello {name:~<30}. Now is {year}')
# print(f'Hello {name:~>30}. Now is {year}')

# a,b,c,d=map(int, input('->').split())
# prod=a*b*c*d
# print(prod)



