# a = 0
# b = 1
# for i in range (0,10):
#     print (f'{i+1}: {a}')
#     # c = b
#     # b += a
#     # a = c
#     a, b = b, a + b


#With generator (NEW CONCEPT FOR ME)

def fib (num):
    a, b = 0, 1
    for i in range (0, num):
        yield f'{i+1}: {a}'
        a, b = b, a + b
    return

fibnumbers = (i for i in fib(10))

for item in fibnumbers:
    print (item)

