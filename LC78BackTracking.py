def subsets(nums):
    res = []

    def backtrack(start, path):

        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(i)

            # recurse
            backtrack(i+1, path)
            
            #backtrack
            path.pop()
        
    backtrack(0, [])
    return res

nums = [1,2,3]
print(subsets(nums))
    
