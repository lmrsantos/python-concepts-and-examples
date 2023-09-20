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