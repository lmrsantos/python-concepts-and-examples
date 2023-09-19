str1="my name is Luiz Marcelo"
list1 = str1.split(" ")
list2 = list1[::-1]
result = [x[::-1] for x in list2]
str2 = " ".join(result)
print (str2)
print (str1[::-1])
print (str1[3:7:1])
list3 = list1[0:len(list1):2]
print (list3)

num = 10000.1324
print (f'${num:,.2f}')
