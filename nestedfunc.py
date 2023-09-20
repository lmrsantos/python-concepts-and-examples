# understanding nested function before talking about decorator (after understanding it check decorator.py)

#NESTED Function
def external(x):
    def internal(y):
        return x + y
    return internal

add_4 = external(4)
result = add_4(6)
print (f'Nested Function: {result}')

# Function as ARGUMENT
def sum_numbers(x, y):
    return x+y

def call_func(func, x, y):
    return func(x, y)

result = call_func(sum_numbers,4,6)

print (f'Function as argument: {result}')

# Calling function as decorator without using decorator
# see the concepts of function as argument and nested functions are present in this solution

def decor_func(func):
    def inter ():
        print ("Do something before the main function")
        func()
        print ("Do something after the function")
    return inter

def main_func():
    print ("I am the main function")
    return

aux = decor_func(main_func)
aux()