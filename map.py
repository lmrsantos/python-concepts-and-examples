# funcl = lambda x,y: x*y
# result = list(map(funcl,[1,2,3,4],[4,3,2,1]))
# print (result)

squares = list(map(lambda x: x**2 if x%2 == 0 else "odd",[1,2,3,4,5,6,7]))
print(squares)

mylist=[]
for i in range(1,10):
    mylist.append(i)

print(mylist)

# with ternary operator
cont = lambda x,y: x**y if y%2 == 0 else y**x
print (cont(2,5))

print (list(map(lambda x: x**2, [1,2,3])))

def square (n):
    return n**2

def double(n):
    return n*2

num = double(3)
print(square(num))


## convert F to C

f = [0, 32, 70, 100, 110]

c = list(map(lambda x: (float(5)/9)*(x-32), f))
for x in c:
    print (f'{x:.2f}')