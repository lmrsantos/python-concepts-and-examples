import psutil

# sum first n numbers
n = 1000000

## Build-in Range
result = sum(range(n))
print (f'----------\nbuild-in range: {result:,}')

# Get the memory usage of the current process
memory_usage = psutil.virtual_memory().percent
print (f'memory usage: {memory_usage}')

# Get the elapse time of the current process
elapse_time1 = psutil.Process().cpu_times().system
proc_name = psutil.Process().name()
proc_pid = psutil.Process().pid
proc = psutil.Process(proc_pid)
print (f'elapse time: {elapse_time1}')
print (proc)

## Yield Generator
def firstn(n):
    result = []
    for i in range(1,n):
        yield i
    return
result  = sum(firstn(n))
print (f'----------\nwith yield: {result:,}')

# Get the memory usage of the current process
memory_usage = psutil.virtual_memory().percent
print (f'memory usage: {memory_usage}')

# Get the elapse time of the current process
elapse_time2 = psutil.Process().cpu_times().system
proc_name = psutil.Process().name()
proc_pid = psutil.Process().pid
proc = psutil.Process(proc_pid)
print (f'elapse time: {elapse_time2}/{elapse_time2-elapse_time1}')
print (proc)
# proc.kill()

## Traditional Function
def firstn(n):
    result = []
    for i in range(1,n):
        result.append(i)
    return result

result  = sum(firstn(n))
print (f'----------\ntraditional: {result:,}')

# Get the memory usage of the current process
memory_usage = psutil.virtual_memory().percent
print (f'memory usage: {memory_usage}')

# Get the elapse time of the current process
elapse_time3 = psutil.Process().cpu_times().system
proc_name = psutil.Process().name()
proc_pid = psutil.Process().pid
proc = psutil.Process(proc_pid)
print (f'elapse time: {elapse_time3-elapse_time2}')
print (proc)



