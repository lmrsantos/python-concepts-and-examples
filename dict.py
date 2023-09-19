#DICTIONARY

from collections import defaultdict
#Build list with students' name and grades
examgrades = [('Bob',100),('Mary',100),('Rich',95),('Rich', 74),('Mary', 87), ('Bob',96)]

#Consolidate grades per student
# studentgrades = {}
studentgrades = defaultdict(list)

for name, grades in examgrades:
    if name not in studentgrades:
        studentgrades[name] = []
    studentgrades[name].append(grades)

#Build list with final grade per student
finalgrade = {}
for name, grades in studentgrades.items():
    avrgrade = 0
    contgrades = 0
    for grade in grades:
        avrgrade += grade
        contgrades += 1
    finalgrade[name]=avrgrade

print (studentgrades)
print (finalgrade)

sorted_scores = dict(sorted(finalgrade.items(), key=lambda item: item[1]))
print(sorted_scores)



#define dict

cars = dict(brand=[], year=[],model=[])

#add cars (brand, year, model)

cars['brand'].append('Mercedes')
cars['year'].append(2019)
cars['model'].append('GLE')
cars['brand'].append('BMW')
cars['year'].append(2032)
cars['model'].append('X5')
print (cars)

#find index
i=cars['brand'].index('BMW')
print(i)

#update cars year

cars['year'][i]=2023
print (cars['year'][i])

#delete car
del cars['brand'][i]
del cars['year'][i]
del cars['model'][i]
print (cars)