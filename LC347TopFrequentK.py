from typing import List
from typing import Counter

'''
Approach
------------
Frequency Mapping: We initialize a Counter object with the input list nums. This creates a dictionary-like 
structure where keys are the numbers and values are their frequencies.
Top-K Selection: We call the .most_common(k) method. Internally, Python uses a Heap data structure to find 
the k elements with the highest frequencies. This is more efficient than sorting the entire dictionary if k is 
significantly smaller than the total number of unique elements.
Result Extraction: Since most_common(k) returns a list of tuples (e.g., [(element, frequency)]), we use a list 
comprehension to extract only the element (the first item in the tuple) and return it.
'''
def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    result = [n for n, tot in count.most_common(k)]    
    return result

nums = [1,1,1,2,2,3,3,3,3,4]
k = 2
print(topKFrequent(nums, k))