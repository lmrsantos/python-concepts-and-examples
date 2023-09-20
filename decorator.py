# After understanding nested functions now we can talk about decorators
# advantage of decorators is that you do not need to change your main function to apply some small changes in the code
# you just need to change to decorator function

def decor_func(func):
    def inter ():
        print ("Do something before the main function")
        func()
        print ("Do something after the function")
    return inter

#syntax to add the decorator: start with @ and then function name
@decor_func
def main_func():
    print ("I am the main function")
    return

main_func()

print ("--------")

def func_out(func,x,y,z):
    def func_inner():
        print ("before")
        func(x,y,z)
        print ("after")
    return func_inner

def soma(x, y, z):
    print (f'{x+y-z:,}')

a = func_out(soma, 79243, 22340, 1583)
a()


def func_outter(func):
    def func_inner(x,y):
        print ("---------\nbefore")
        if y == 0:
            print ("Cannot divide by 0")
        else:
            func(x,y)
        print ("after")
    return func_inner

@func_outter
def calc(x, y):
    print (f'{x/y:,.2F}')

calc(4,2)
calc(4,0)

