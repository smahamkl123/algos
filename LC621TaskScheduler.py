from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # find the task that is most frequently being scheduled
        ctr = Counter(tasks)
        f = ctr.most_common(1)[0]

        # find total tasks that are as freuent as the most frequent one
        o = len([l for l in ctr.values() if l == f[1]])

        # the formula is (f-1)*(n + 1) + total tasks
        return max((f[1]-1) * (n + 1) + o, len(tasks))


s= Solution()
tasks = ["A","A","A","B","B","B"]
tasks = ["A","C","A","B","D","B"]
n = 2
m = 1
print(s.leastInterval(tasks, n))
