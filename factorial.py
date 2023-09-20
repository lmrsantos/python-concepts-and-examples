# to make this type of code I strong recommend to think and test your logic outside of the code. First open a blank sheet 
# (or a spreadsheet) and test your hypotesis and alternative solutions. Only after you make sure it is working, jump into
# the codification

import math
import copy
def calccombination(list):
    combinations=[]

    def swapelements(list, indexbase, startswap, firstswap, nextswap, limit):

        if len(list) < 2:
            firstswap = 0
            nextswap = 0

        if nextswap <= limit:
            auxlist = copy.deepcopy(list)
            # alternative below to copy.deepcopy()
            # auxlist = []
            # auxlist = [element for index, element in enumerate(list)]
            aux = auxlist[firstswap]
            auxlist[firstswap]=auxlist[nextswap]
            auxlist[nextswap]=aux
        if len(combinations) == 0:
            combinations.append(auxlist)
        else:
            totalpossibilities = math.factorial(len(list))
            if len(combinations) == totalpossibilities:
                return
            else:
                if nextswap > limit:
                    if len(combinations) % (math.factorial(len(list))/len(list)) != 0:
                        startswap = 0
                        firstswap = 1
                    else:
                        return
                else:
                    if len(combinations) % (math.factorial(len(list))/len(list)) == 0 and indexbase != 0:
                        return 
                    else:
                        startswap += 1
                        if firstswap == 0:
                            firstswap = 1
                        else:
                            firstswap += 1
                    combinations.append(auxlist)
            indexbase = -1

        for i in range(startswap, len(list)):
            if indexbase == 0 and len(combinations) > 1: 
                firstswap = 0
                nextswap = i
            elif indexbase == 0 and len(combinations) == 1 and len(list) == 2:
                firstswap = 0
                nextswap = 1
            else:
                nextswap = firstswap + 1
            swapelements(combinations[indexbase], indexbase, startswap, firstswap, nextswap, len(list)-1)

    swapelements(list, 0, 0, 1, 1, len(list)-1)
    return (combinations)
list=['A', 'B', 'C', 'D']		
finalcomb = calccombination(list)

import csv
##open as csvfile and instance a variable (e.g. writer) with csv.writer passing csvfile as argument
with open ("comb.csv","w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    #write calling <instaciated variable>.writerow / commands below must be inside with open command
    for index, elements in enumerate(finalcomb):
        print (f'{index} - {elements}')
        writer.writerow([index, elements])