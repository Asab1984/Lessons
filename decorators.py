# def simpleDecorator(myFunction):
#     print('Hello! I am decorator')
#     def simpleWrapper():
#         print('Functions starts working...')
#         myFunction()
#         print('See you!')
#
#     return simpleWrapper()
#
# def simpleDecorator_v2(myFunction):
#     print('Hello I am second decorator')
#     def simpleWrapper():
#         print('Lets start...')
#         myFunction()
#         print('Good luck!')
#     return simpleWrapper
#
# @simpleDecorator_v2
# @simpleDecorator
# def sayHi():
#     print('Welcome')
# sayHi()
#
# def sayBye():
#     print('Bye')
#
# sayBye=simpleDecorator(sayBye)
# sayBye()
'''def simpleDecorator_v3(myfunction):
    print('I m 3rd decorator')
    def simpleWrapper():
        print('Functions starts working...')
        result1=myfunction()
        print('See you!')
        return result1
    return simpleWrapper

def calculateSum():
    print('Welcome! lets start calculate')
    x=int(input('x:'))
    y = int(input('y:'))
    return x+y
a=simpleDecorator_v3(calculateSum)
print(a())'''

def simpleDecorator_v4(myfunction):
    print('Hello! Im fourth Decorator')
    def simpleWrapper(argX, argY):
        print('I have got {}, {}. Function starts working...'.format(argX,argY))
        result1=myfunction(argX,argY)
        print('See you!')
        return result1
    return simpleWrapper
def calculateSum(a,b):
    print('Welcome! lets start calculate')
    x=int(input('x:'))
    y = int(input('y:'))
    return x+y+a+b

a=simpleDecorator_v4(calculateSum)
print(a(3,4))






# simpleDecorator(sayHi)

