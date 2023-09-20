# Deepcopy and shallow copy. It is important specially when treating with multiple dicts and lists using them as parameters 
# or as auxiliar for some logic. In additional, you can see an application for IS operator 

import copy

list1 = [1,2,3,4,5]
list2 = list1
list3 = copy.deepcopy(list1)
list4 = copy.copy(list1)
print (f'list 2 is list1? {list2 is list1}')
print (f'list 3 is list1? {list3 is list1}')