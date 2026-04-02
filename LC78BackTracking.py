'''
Decision Tree (Example: [1,2,3])
Start []
 ├── include 1 → [1]
 │    ├── include 2 → [1,2]
 │    │    ├── include 3 → [1,2,3]
 │    │    └── exclude 3 → [1,2]
 │    └── exclude 2 → [1]
 │         ├── include 3 → [1,3]
 │         └── exclude 3 → [1]
 └── exclude 1 → []
      ├── include 2 → [2]
      │    ├── include 3 → [2,3]
      │    └── exclude 3 → [2]
      └── exclude 2 → []
           ├── include 3 → [3]
           └── exclude 3 → []
'''
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
    
