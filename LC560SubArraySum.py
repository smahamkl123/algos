from typing import List
from typing import Counter

def subarraySum(nums: List[int], k: int) -> int:
    prefix_sum = 0
    prefix_map = {0:1}
    count = 0

    for num in nums:
        prefix_sum += num

        if (prefix_sum - k) in prefix_map:
            count += prefix_map[prefix_sum - k]
        
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
    
    return count
 
    

nums = [1,2,1,2,1]
# nums = [1,1,1]
k = 3
print(subarraySum(nums, k))