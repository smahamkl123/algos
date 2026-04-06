import heapq

class MedianFinder:

    def __init__(self):
        self.small = [] # max pq - left side (use negative nums)
        self.large = [] # min pq - right side
        

    def addNum(self, num: int) -> None:
        #first add num to the left queue
        heapq.heappush(self.small, -num)


        #first find out which pq(left/right) the new number to be added
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        

        #balance sizes, left one is supposed to be equal or greater(in case of odd number of elements)
        if len(self.small) > (len(self.large) + 1):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        
        return (-self.small[0] + self.large[0])/2
        


#Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
obj.addNum(3)
param_2 = obj.findMedian()
print(param_2)