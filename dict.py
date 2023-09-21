#DICTIONARY

from collections import defaultdict
#Build list with students' name and grades
examgrades = [('Bob',100),('Mary',100),('Rich',95),('Rich', 74),('Mary', 87), ('Bob',96)]

#Consolidate grades per student
# studentgrades = {}
studentgrades = defaultdict(list)

for name, grades in examgrades:
    # 2 lines below are not necessary because the list was defined with defaultdict, otherwise the list must be initialized with empty []
    # if name not in studentgrades:
    #     studentgrades[name] = []
    studentgrades[name].append(grades)

#Build list with final grade per student
finalgrade = {}
for name, grades in studentgrades.items():
    avrgrade = 0
    contgrades = 0
    for grade in grades:
        avrgrade += grade
        contgrades += 1
    finalgrade[name]=f'{avrgrade/contgrades:.2f}'

print (studentgrades)
print (finalgrade)

sorted_scores = dict(sorted(finalgrade.items(), key=lambda item: item[1]))
print(sorted_scores)
