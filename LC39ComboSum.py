from typing import List


'''
Combination Sum. Use backtracking: pick numbers from a starting index, reuse the same index (because repeats are allowed), 
and move forward to the next index when you’re done with that branch so you don’t build the same multiset in a different order.
'''
def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    res = []
    path = []

    def backtrack(start, remainingSum):
        if remainingSum == 0:
            res.append(path[:])
            return
        if remainingSum < 0:
            return
        
        for i in range(start, len(candidates)):
            path.append(candidates[i])

            backtrack(i, remainingSum - candidates[i])

            path.pop()
    
    backtrack(0, target)

    return res

candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))
