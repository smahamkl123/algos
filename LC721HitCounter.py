from typing import List
from bisect import bisect_left

# https://algo.monster/liteproblems/362

class HitCounter:
    """
    A hit counter that tracks hits and returns the number of hits
    in the past 300 seconds (5 minutes).
    """

    def __init__(self):
        """Initialize the hit counter with an empty list to store timestamps."""
        self.timestamps: List[int] = []

    def hit(self, timestamp: int) -> None:
        """
        Record a hit at the given timestamp.

        Args:
            timestamp: The current timestamp (in seconds granularity)
        """
        self.timestamps.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 300 seconds from the given timestamp.

        Args:
            timestamp: The current timestamp (in seconds granularity)

        Returns:
            The number of hits in the range [timestamp - 299, timestamp]
        """
        # Find the leftmost position where (timestamp - 299) could be inserted
        # to maintain sorted order. This gives us the index of the first hit
        # that falls within our 300-second window
        start_of_window = timestamp - 300 + 1
        first_valid_index = bisect_left(self.timestamps, start_of_window)

        # All hits from first_valid_index to the end are within the window
        return len(self.timestamps) - first_valid_index


# Your HitCounter object will be instantiated and called as such:
obj = HitCounter()
obj.hit(1)
obj.hit(1)
print(obj.getHits(300))
