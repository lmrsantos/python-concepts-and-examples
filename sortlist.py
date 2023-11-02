import random
import time
start_time = time.time()
start = 0
a = random.sample(range(100),100)
swap = True
while swap:
    swap = False
    i = start
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
            start = i
            swap = True
            break
end_time = time.time()
elapse_time = end_time - start_time
print (f'func1:{elapse_time}')
print (a)