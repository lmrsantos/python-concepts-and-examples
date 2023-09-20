def findCombination(listnumbers, target):
    result = []
    def sumNumbers(listnumbers, current_index, current_sum, current_combination, target):
        if current_sum == target:
            result.append(current_combination)
            return
        if current_sum > target:
            return
        for cont in range(current_index, len(listnumbers)):
            sumNumbers(listnumbers, cont, current_sum + listnumbers[cont],current_combination + [listnumbers[cont]], target)

    sumNumbers(listnumbers, 0, 0, [], target)
    return result
    
result = findCombination([2,3,4],17)
print (result)
