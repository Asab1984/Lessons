#Двійкові файли
#документи і електронні таблиці .doc .pdf .xls
#архіви .zip .7z .rar .iso
#бази даних .db .mdb .sqllite .accde
#Виконувані файли .exe .dll
#зображення .png .jpeg .gif
#аудіо .mp3 .mka
#відео .mp4 .avi

#Текстові файли
#Текстові документи .txt .rtf .tex
#файли початкових кодів .py .js .java .c .cpp
#Web документи і стандарти JSON HTML CSS XML
#Файли налаштувань та конфігурацій .cfg .ini

#Відкриття файлу
#Чистання з  файлу
#Запис  у файл
#Видалення

#fileObj = open(fileName, mode)
#r
#w
#a
#r+
#w+
#a+
#rb
#wb
#ab
#wb+
#ab+
'''f1=open('C:\\Python\\Files\\myfile1.txt', 'r')
s1=f1.readline() #прочитати строку
print(s1)
s2=f1.readline()
print(s2)'''
'''f1=open('C:\\Python\\Files\\myfile1.txt', 'r')
print(f1.read()) #read - читання
print(f1.read(4)) #read(n) - n-кількість символів для читання
print(f1.read(4))'''
# f1=open('C:\\Python\\Files\\myfile1.txt', 'r')
# lines=f1.readlines() #зчитати файл у список рядків
# print(lines)
'''f1=open('C:\\Python\\Files\\myfile1.txt', 'r')
for line in f1:
    print(line)'''
'''f2=open('C:\\Python\\Files\\myfile2.txt','w')
n=f2.write('Some text')'''
# import random
# i=0
# spysok=[]
# while i<10:
#     chislo=random.randint(0,1001)
#     spysok+=[chislo]
#     i+=1
# print(spysok)
# f=open('C:\\Python\\Files\\spysok.txt', 'w')
# s=str(len(spysok))
# f.write(s+'\n')
# for i in spysok:
#     s=str(i)
#     f.write(s+' ')
# f.close()
'''f=open('C:\\Python\\Files\\spysok.txt', 'r')
lines=f.readlines()
print(lines)'''
# spysok_txt=['dasd','asdasd','adsdas','adasdas','dasda']
# f = open('C:\\Python\\Files\\spysok_strok.txt', 'w')
#
# for line in spysok_txt:
#     f.write(line+'\n')
#
# f.close()
'''spysok_txt=['fsdfgdg','asdfdgfdasd','adsdddadas','asdawsd','werwerwer']
f = open('C:\\Python\\Files\\spysok_strok.txt', 'w')

for line in spysok_txt:
    f.write(line+'\n')

f.close()'''
# slovnyk = {1:'Mon', 2:'Tue', 3:'Wed', 4:'Thu', 5:'Fri'}
# f = open('C:\\Python\\Files\\slovnyk.txt', 'w')
# for item in slovnyk:
#     s=str(item)
#     s+=':'
#     s+=slovnyk.get(item)
#     s+='\n'
#     f.write(s)
#
# f.close()
'''f1=open('C:\\Python\\Files\\myfile1.txt', 'r')
count=0
s = f1.readline()
while s != '':
    s = f1.readline()
    count+=1
print(count)'''

# f2=open('C:\\Python\\Files\\myfile1.txt', 'r')
# spysok=f2.readlines()
# count=len(spysok)
# print(count)

'''f3=open('C:\Python\Files\python.txt', 'r')
s=input('Enter text for change:')
pos=int(input('enter pos:'))
spysok=f3.readlines()
if (pos>=0) and (pos<len(spysok)):
    if (pos==len(spysok)-1):
        spysok[pos]=s
    else:
        spysok[pos] = s + '\n'
f3.close()
f3=open('C:\Python\Files\python.txt', 'w')
for line in spysok:
    f3.write(line)
f3.close()
'''

# pos = int(input('pos='))
# f=open('C:\Python\Files\python.txt', 'r')
# spysok=f.readlines()
# if (pos>=0) and (pos<len(spysok)):
#     i=pos
#     while i<len(spysok)-1:
#         spysok[i]=spysok[i+1]
#         i+=1
#     spysok=spysok[:-1]
# f.close()
# f=open('C:\Python\Files\python.txt', 'w')
# for line in spysok:
#     f.write(line)
# f.close()
'''f1=open('C:\Python\Files\myfile1.txt', 'r')
f2=open('C:\Python\Files\myfile2.txt', 'r')

spysok1=f1.readlines()
spysok2=f2.readlines()
spysok3=spysok1+['\n']+spysok2

f1.close()
f2.close()

f3=open('C:\Python\Files\\file3.txt', 'w')
for i in spysok3:
    f3.write(i)
f3.close()
'''
spysok=[]
while True:
    a=input('Чи хочете ви ввести нову строку? y or n')
    if a == 'y':
        b=input('Enter line:')
        spysok+=[b]
    elif a=='n':
        break

print(spysok)



