from typing import List
from collections import deque

class Solution:

    def maxSlidingWindow(nums, k):
        dq = deque()
        res = []

        for i in range(len(nums)):

            # 1. Remove out-of-window indices
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # 2. Remove smaller elements
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # 3. Add current index
            dq.append(i)

            # 4. Add to result
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3