# list stack and queue

# stack last come in first come out (LIFO)
print ("-------> STACK (LIFO) <--------")
stack = []
stack.append(1)
stack.append(2)
po_stack = stack.pop()
print (stack, po_stack)

# queue first come in first come out (FIFO)
print ("\n-------> QUEUE (FIFO) <--------")
queue = []
queue.append(1)
queue.append(2)
po_queue = queue.pop(0)
print (queue, po_queue)
print (f'***** {queue[0]}')

# collections 
print ("\n-------> Collections <--------")
from collections import Counter
list1 = [1,2,3,4,5,5,4,5,3,5,1]

countlist = Counter(list1)
print (countlist.most_common(1))

# Enumerate
print ("\n-------> ENUMERATE <--------")
list2 = [1,2,3,4,5]
print (list2.index(2))
for index, element in enumerate(list2):
    print (index, element)
print (list2[0])

# Sliding
print ("\n-------> RANGE LIMIT + SLIDING <--------")
word = "ABC"
list3 = [letter for letter in word]
for i in range(0,len(list3)):
    print (list3[i])

print(list3[::-1])

# comprehension list
print ("\n--------> COMPREHENSION LIST <-------------")
l = []
l = [[i**2, i**3] for i in range (5)]
print (l)

# SHALLOW COPY
print ("\n--------> LIST SHALLOW COPY <-------------")
lst = [3,4,1,5,2]
print (f'original list: {lst}')
copylist = lst
lst.append(6)
print (f"copy list: {copylist}")
print (f"original list after append 6: {lst}")
print (f"copy list after append 6: {copylist}")
print (f"                                          ^")

# DEEP COPY
print ("\n--------> ALTERNATIVE FOR DEEP COPY <-------------")
lst = [3,4,1,5,2]
print (f'original list: {lst}')
copylist = []
copylist = [element for index, element in enumerate(lst)]
print (f"copy list: {copylist}")
lst.append(6)
print (f"original list after append 6: {lst}")
print (f"copy list after append 6: {copylist}")

# L I S T   F U N C T I O N S
print ("\n--------> LIST FUNCTIONS <-------------")
lst = [3,4,1,5,2]
print (f'original list: {lst}')

# 1 - sort()
lst.sort()
print (f'{lst} <--- sorted list')

# 2 - append()
lst.append(6)
print (f'{lst} <--- appended list')

# 3 - extend()
lst.extend(["a","b", "c"])
print (f'{lst} <--- extended list')

# 4 - index()
print (f'{lst[6]} <--- index 6')

# 5 - pop
lst.pop(8)
lst.pop(7)
lst.pop(6)
print (f'{lst} <--- pop indexes 6, 7, 8')

# 6 - max()
print (f'{max(lst)} <--- max')

# 7 - min()
print (f'{min(lst)} <--- min')

# 8 - len()
print (f'{len(lst)} <--- lenght')

# 9 - list()
tpl = (5,6,7,8,9)
lst1 = list (tpl)
print (f'{lst1} <--- lst1 = list of a tuple')

# 10 - compare()
print (f'{(lst == lst1)} <--- compare lst and lst1 with ==')

#11 - type()
print (f'{type(lst)} <--- type')