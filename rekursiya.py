
"""b=0
for i in spysok:
    b+=i

print(b)"""
# spysok=[2,4,7,12,34,1,56,78,9]
# def calcSum(A):
#     if A==[]:
#         return 0
#     else:
#         summ=calcSum(A[1:])
#         summ+=A[0]
#         return summ
#
# summ=calcSum(spysok)
# print(summ)
'''spysok=[1, -7, 9 , 15, 25,-67, -98,-56, 65]
def calcSumNegative(A):
    if A==[]:
        return 0
    else:
        count=calcSumNegative(A[1:])
        if A[0]<0:
            count+=1

        return count

n=calcSumNegative(spysok)
print(n)'''
# def GetFibonacciList(n,l):
#     count=len(l)
#     if len(l)<2:
#         return []
#
#     num1=l[count-2]
#     num2=l[count-1]
#
#     if (num1+num2)<n:
#         l=l+[num1+num2]
#         return GetFibonacciList(n, l)
#     else:
#         return l
# new=GetFibonacciList(100, [0,1])
# print(new)
'''def Power(x,y):                   #1. Power(3,4) .... #1. 2. 3. 4. #3*3*3*3
    if y>0:                       #1. 4>0 ->
        return x*Power(x, y-1)    #1. 3*Power(3,3)
    else:
        return 1

x=3
y=4
res=Power(x,y)
print(res)'''

# def GetMaxList(L):
#     if len(L)>1:
#         Max=GetMaxList(L[1:])
#         if L[0]<Max:
#             return Max
#         else:
#             return L[0]
#
#     if len(L)==1:
#         return L[0]
#
# spysok=[500,6000,40,53]
# print(res)
a=int(input('кількість елементів'))
i=0
b=[]
while i<a:
    s=int(input('chislo:'))
    b+=[s]
    i+=1
print(b)

