# # list stack and queue

# # stack last come in first come out

# stack = []
# stack.append(1)
# stack.append(2)
# po_stack = stack.pop()
# print (stack, po_stack)

# queue = []
# queue.append(1)
# queue.append(2)
# po_queue = queue.pop(0)
# print (queue, po_queue)
# print (f'***** {queue[0]}')

# from collections import Counter

# list1 = [1,2,3,4,5,5,4,5,3,5,1]

# countlist = Counter(list1)
# print (countlist.most_common(1))


# list2 = [1,2,3,4,5]
# print (list2.index(2))
# for index, element in enumerate(list2):
#     print (index, element)

# print (list2[0])

# word = "ABC"

# list3 = [letter for letter in word]
# for i in range(1,len(list3)):
#     print (list3[i])

# print(list3[-1])

# l = []
# a = []
# l1 = []
# l = [[i**2, i**3] for i in range (5)]

# for i in range(5):
#     a.append(i**2)
#     print (f'a: {a}')
#     l1.append(a)
#     print (l1)

# a = []
# l1 = []

# for i in range(3,4):
#     new_list = []
#     for j in range(i + 1):
#         print (j)
#         new_list.append(j**2)
#     l1.append(new_list)

# # Print the list l1
# print(l1)

word = "water"
print (not word.isalpha())