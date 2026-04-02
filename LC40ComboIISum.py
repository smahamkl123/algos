from typing import List

'''
LeetCode 40
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates 
where the candidate numbers sum to target. Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.
'''
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = list()
    path = list()
    candidates.sort()

    def backtrack(start, remainingSum):
        if remainingSum == 0:
            res.append(path[:])
            return
        if remainingSum < 0:
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i -1]:
                continue

            path.append(candidates[i])

            backtrack(i+1, remainingSum - candidates[i])

            path.pop()
    
    backtrack(0, target)

    return list(res)

candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum(candidates, target))
