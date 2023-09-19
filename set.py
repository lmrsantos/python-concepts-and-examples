# set is unique result from list of values

#lists

set1 = set([1,2,3])
set2 = set([3,4,5])
set1.add(6)
set2.pop()
set1.pop()
print (set1, set2)
inter = set1&set2
uni = set1|set2
exc = set1^set2
print (inter, uni, exc)

