# l = []
# t=[]
# for i in range(3):
#     l.append(i)
# t.append(tuple(l))
# print (t)
# l=[]
# for i in range(3,6):
#     l.append(i)
# t.append(tuple(l))
# print (t)

# tuples = []
# tuples.append((1))

def outter (func):
    def inner(x, y):
        print ("before")
        if y == 0:
            print ("divisor cannot be zero")
        else:
            func(x,y)
        print ("after")
    return inner
@outter
def divfunc(x,y):
    print (f'{x} divide by {y} is {x/y}')
    return

divfunc(10,90)
# def func_out(func,x,y,z):
#     def func_inner():
#         print ("-------\nbefore")
#         func(x,y,z)
#         print ("after")
#     return func_inner

# def soma(x, y, z):
#     print (f'{x+y-z:,}')

# a = func_out(soma, 79243, 22340, 1583)
# a()

import classx as x

print ("------- TEST----------" )
son = x.GrandSon("grandson")
son.grandPaFunc("grandson")