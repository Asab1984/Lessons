"""myDict = {'key1':1, 'key2':2,"key3":True}
myDict2 = {1:'student', 2:'admin'}
print(myDict)
print(myDict2)

A={}
print('A = ', A)

B={1:'Mon', 2:'Tue', 3:'Wed', 4:'Thu'}
print(B)
print(B[2])

slovnyk_zn={'Pi':3.1415, 'Exp':1.71}
print(slovnyk_zn)
print(slovnyk_zn['Exp'])

slovnyk_nabir={'spysok1':[1,2,'hello'], 'spysok2':[8,10,False]}
print(slovnyk_nabir)
print(slovnyk_nabir['spysok1'])
print(slovnyk_nabir['spysok1'][2])"""

# pustiy_slovnyk=dict()
# print(pustiy_slovnyk)
#
# weak=dict(Monday=1, Tuesday=2, Wenesday=3)
# print(weak)
#
# Days=[1,2,3]
# days_names=['Mon','Tue',"Wed"]
# all_days=dict(zip(Days, days_names))
# print(all_days)
#
# pairs_dict=dict([(1,'Winter'),(2,'Summer'),(3,'Spring')])
# print(pairs_dict)

"""weak=dict(Monday=1, Tuesday=2, Wenesday=3)
value=weak['Monday']
print(value)

pairs_dict=dict([(1,'Winter'),(2,'Summer'),(3,'Spring')])
print(pairs_dict[2])"""

"""slovnyk={1:'Python',2:'C++',3:'C#', 4:'SQL'}
# a=slovnyk[5]
# print(a)

mova=int(input('enter your lang ->'))

if mova in slovnyk:
    print('Mova', slovnyk[mova])
else:
    print('Error')"""

# slovnyk1={'programmer1':'Python', 'programmer2':'C++'}
# slovnyk2={'workers':slovnyk1}
# print(slovnyk1)
# print(slovnyk2)
# slovnyk3={'workers':{'programmer1':'Python', 'programmer2':'C++'}}
# print(slovnyk3)

"""slovnyk1={'programmer1':'Python', 'programmer2':'C++'}
print(len(slovnyk1))

position = {'Admin':{'Admin1', 'Admin2', 'Admin3}, 'Programmers':{'Python', 'C++'}}
print(len(position))
print(len(position['Admin']))"""

# days={1:'Python',2:'C++'}
# print(days[1])
# days[2]="C#"
# days[3]='SQL'
# print(days)
# del days[3]
# print(days)

"""words=dict()
count=int(input('kilkist sliv: '))
i=0
while i<count:
    kluch=input('Enter key')
    znachennya=input('Enter value')

    if kluch not in words:
        words[kluch]=znachennya

    i+=1
print(words)"""

# diction={1:'1',2:'2'}
# print(diction)
# diction.clear()
# print(diction)
#
# diction1={'A':2, 'B':2}
# d2=diction1.copy()
# print(diction1)
# print(d2)
# diction1['C']=3
# d2['A']='one'
# print(diction1)
# print(d2)
#
# d3=dict.fromkeys([1,2,3]) #створити новий словник з ключів
# print(d3)
#
# d4=dict.fromkeys([1,2],'A')
# print(d4)
#
# d5=dict.fromkeys([1,2],['A','B'])
# print(d5)
#
# d6={'1':'o','2':'b'}
# n=d6.items() # список пар ключів та значень
# print(n)
# n2=dict.items(d6)
# print(n2)
#
# d7= {1:"a", 2:'b'}
# n3=d7.keys() #список ключів
# print(n3)
# n4=iter(d7)
# print(list(d7))
# print(n4)
# n5=d7.values()
# print(n5)
# print(list(n5))
#
# d8={1:'a', 2:'b', 3:'c', 4:'d'}
# item=d8.pop(2) #видалення елемента зі словника і витягуємо у змінну його значення
# print(item)
# print(d8)
#
# d9={1:'a', 2:'b', 3:'c', 4:'d'}
# item=d9.popitem() #видаляє останню пару зі словника і записує її у змінну
# d10={'1':'A','2':'B'}
# item2=d10.popitem()
# print(item)
# print(item2)
# print(d9)
# print(d10)
#
# d11={'R':1, 'B':2, 'G':3}
# item=d11.setdefault('G')
# print(item)
# print(d11)
#
# item2=d11.setdefault('W')
# print(item2)
# print(d11)
#
# item3=d11.setdefault('H',8)
# print(item3)
# print(d11)
#
#
# d12={'A':1,'B':2}
# d12.update([('C',3),('D',4)])
# print(d12)
#
# d12.update([('C',15),('D',24)])
# print(d12)



"""users = [{'name':'Anna', 'age':10, 'login':'user56'},
        {'name':'Mark', 'age':21, 'login':'user123'},
        {'name':'Jack', 'age':30, 'login':'us54'},
        {'name':'Alice', 'age':16, 'login':'userAlice'}]
keyName=input('Input info type: ')
keyValue=input('Input info value: ')
if keyName=='age' and keyValue.isdigit()==True:
    keyValue=int(keyValue)
isElementFound=False
for user in users:
    if user.get(keyName)==keyValue:
        print('Element is found!')
        for key, val in user.items():
            print('{}:{}'.format(key,val))
        isElementFound=True
        break
if isElementFound==False:
    print('Element is not found')
"""



my_dict={'Nick':{'phone':'0734562312', 'telegram':{'official':'@nick_073','private':'@nick_privat'},'instagram':'@nick_wow'},
        'Ann':{'phone':'0663548765', 'telegram':{'official':'@ann066','private':'@ann_privat'},'instagram':'@ann_new'},
        'Jane':{'phone':'0937865192', 'telegram':{'official':'@jane_093','private':'@jane_privat'},'instagram':'@jane_official'}}
name=input('Enter Name ').title()
contact_type=input('Enter the contact type ').lower()
user=0
try:
    if contact_type == 'telegram ':
        type_tg = input('privat or official ').lower()
        user = my_dict[name][contact_type][type_tg]
        print(user)
    else:
        user = my_dict[name][contact_type]

    print(user)
except KeyError:
    print('U entered not correct info')


# user=my_dict[input('Enter Name ').title()][input("Enter the contact type ").title()]
# print(user)








