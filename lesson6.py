# students = ['Alex', 'Dasha', 'Masha', 'Katy']
# print('Hi', students[1])
# a = [12,10,12,11,10,12]
#
# students.append('Vasya') # add 1 item
# print(students)
# a.extend([11,12,10,9,12]) # add a lot  of item
# print(a)
# a.insert(2,     8)
# #       index  znachennya
#
# print(a)
# print(students[1:5])
# print(', '.join(students))
#
# i = students.index('Dasha')
# print(i, students[i])
# del(students[i])
# print(students)
#
# c = [12,11,10,9]
# print(c)
# c[3] = 11
# print(c)
# print(c[-1])
#
# students.append('Petya')
#
# for item in students:
#     print('Hi', item)
#     print( item, [10,11,12])
#
# for i in range(len(students)):
#     print(i, students[i])


# list1 = [0,1,2,3,4,5,6,7,8,9]
# list2 = ['a','b','c','d','e','f','g']
# print(list1)
# print(list2)
# print(list1[2])
# list2[-1] = 'G'
# print(list2)
# list3=list1+list2
# print(list3)


# b = [     ['Artem', 'Mark'],     ['Roma', 'Katy', 'Dasha'] ]
# print(b[0][0])
# print(b[1][1])

# a = [1,2,3,4]
# b=[5,6,7]
# c=a+b
# print(a)
# print(b)
# print(c)
#
# d = [1, 2, 3]*5
# print(d)
#
# f = [[12,12,12]]+[[0,0,0,0]] * 10
# print(f)


# myList = ['ab', 'bc','cd', 'de']
# print(myList)
# myList[0:2] = ['IT', 'ST', 12]
# print(myList)


a= [1,2,16,4,14,3,4,5,13, 6,7,8,9,15,10,11,12]

a.remove(4) # видаляє перше знайдене значення
print(a)

a.pop(1) # видаляє за індексом
print(a)

val = a.pop(2)
print(a)
print('Видалено ', val)

i = a.index(8) #повертає перше співпадіння
print('i -', i)

#j = a.index(val, start, end)

print(0 in a)

if 0 in a:
    i = a.remove(0)

# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# print(a[1])


a.reverse()
print(a)

# a.copy()
# print(a)
# a.clear()
# print(a)
print('\n')
w = [12,15,47,85,36,95,23,547,52]
print(w)
print(max(w))
print(min(w))
print(sum(w) / len(w))
print(sorted(w))
q = sorted(w, reverse=True)
print(q)

t=[12,12,11,9,13]
r = t.copy()
t[0]=99
print(t)
print(r)


import random

nums = []
for i in range(100):
    nums.append(random.randint(-100,100))
print(nums)