# understanding nested function before talking about decorator (after understanding it check decorator.py)

def external(x):
    def internal(y):
        return x + y
    return internal

add_4 = external(4)
result = add_4(6)
print (result)
print (type(add_4))