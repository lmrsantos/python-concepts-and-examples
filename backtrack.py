def combinationSum(candidates, target):
    answer = []
    print (f'len(candidates:{len(candidates)}')
    def combinationSumHelper(candidates, current_index, current_sum, current_combination, target):
        print (f'current_sum:{current_sum}')
        print (f'current_combination:{current_combination}')
        if current_sum == target:
            answer.append(current_combination)
            print (f'>>>>>>>>>>>>>>>>>>>>>>>>>>>answer:{answer}')
            return
        if current_sum > target:
            return
        for i in range(current_index, len(candidates)):
            print (f'i:{i}')
            print (f'current_combination inside for:{current_combination}')
            combinationSumHelper(candidates, i, current_sum + candidates[i],current_combination + [candidates[i]], target)
            print (f'i after:{i}')

    combinationSumHelper(candidates, 0, 0, [], target)
    return answer

print (combinationSum([2,3,5],8))