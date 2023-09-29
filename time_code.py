# Find elapse time of a code using time
import time

def outtter(func):
    def inner(n):
        start_time = time.time()
        func(n)
        end_time = time.time()
        elapse_time = end_time - start_time
        print (f'{func.__name__}:{elapse_time}')
    return inner

# @outtter
def func1(n):
    return [str(i) for i in range(n)]

# @outtter
def func2(n):
    return list(map(str,range(n)))

start_time = time.time()
num = 10000
func1(num)
end_time = time.time()
elapse_time = end_time - start_time
print (f'func1:{elapse_time}')

start_time = time.time()
num = 10000
func2(num)
end_time = time.time()
elapse_time = end_time - start_time
print (f'func2:{elapse_time}')