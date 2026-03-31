from typing import List

def moveZeroes(nums: List[int]) -> None:
    tot_non_zeros = 0

    for i in range(len(nums)):
        if(nums[i] != 0):
            nums[tot_non_zeros] = nums[i]
            tot_non_zeros += 1
    
    for i in range(tot_non_zeros, len(nums)):
        nums[i] = 0


nums = [0,1,0,3,12]
nums = [0]
nums = [-1,0,0,1,0]
moveZeroes(nums)

print(nums)