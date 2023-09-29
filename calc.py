
def add_func(a, b):
    return a+b

def subtract_func(a,b):
    return a-b

def multiple_func(a,b):
    return a*b

def divide_func(a,b):
    if b == 0:
        raise ValueError ("divisor cannot be 0")
    
    return round(a/b,2)

