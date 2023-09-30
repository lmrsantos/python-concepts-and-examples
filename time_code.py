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

print ('===> WITH TIME')
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


# The same using timeit
import timeit

print ('===> WITH TIMEIT')

# TEST for FUNC1()
# This is the statement that will runs n times
stmt1 = '''
    func1(100)
'''
# This is the command that will run ONCE in the beginning
setup1 = '''
def func1(n):
    return [str(i) for i in range(n)]
'''
# number refers to how many times the statement will run/loop
elapse_time1 = timeit.timeit(stmt1, setup1, number=1000000)
print (f'func1:{elapse_time1}')

# TEST for FUNC2()
stmt2 = '''
    func2(100)
'''
setup2 = '''
def func2(n):
    return list(map(str,range(n)))
'''
# number refers to how many times the statement will run/loop
elapse_time2 = timeit.timeit(stmt2, setup2, number=1000000)
print (f'func2:{elapse_time2}')

