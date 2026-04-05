from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:

    intervals.sort(key= lambda x: x[0])

    res = []
    temp = intervals[0]

    for i in range(1, len(intervals)):
        
        #check the tmp[1] > intervals[i][0] if so merge
        if temp[1] >= intervals[i][0]:
            #time to merge
            temp[1] = max(temp[1], intervals[i][1])
        else:
            res.append(temp)
            temp = intervals[i]
        
    res.append(temp)

    return res


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))