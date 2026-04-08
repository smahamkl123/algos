from typing import List

'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product 
of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''
def productExceptSelf(nums: List[int]) -> List[int]:
    res = [1] * len(nums)
    prefix = 1
    suffix = 1

    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    print(res)
    for i in range(len(nums)-1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    
    return res

nums = [1,2,3,4]

print(productExceptSelf(nums))
