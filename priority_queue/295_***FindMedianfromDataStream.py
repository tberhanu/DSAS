from typing import List
import heapq

class MedianFinder:
    """
    Design Choice: 
        if odd number of nums, put the EXTRA to maxHeap (ok to make minHeap too)
    minHeap to hold the nums to the RIGHT, the bigger ones
    maxHeap to hold the nums to the LEFT, the smaller ones

    [1, 2, 3, 4,             5, 6, 7, 8, 9]
      maxHeap                  minHeap
    """

    def __init__(self):
        self.minHeap, self.maxHeap = [], []

    def addNum(self, num: int) -> None:
        N, M = len(self.minHeap), len(self.maxHeap)
        if M == 0:
            heapq.heappush(self.maxHeap, -num)
        else:
            if num <= -self.maxHeap[0]:
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.minHeap, num)

        # balancing
        N, M = len(self.minHeap), len(self.maxHeap)
        if M > N + 1:
            smallest = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, smallest)
        elif N == M + 1:
            highest = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -highest)


    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + -self.maxHeap[0]) / 2
        elif len(self.maxHeap) == len(self.minHeap) + 1:
            return -self.maxHeap[0]


class MedianFinder2:
    """
    Design Choice: 
        if odd number of nums, put the EXTRA to minHeap (ok to make maxHeap too)
    minHeap to hold the nums to the RIGHT, the bigger ones
    maxHeap to hold the nums to the LEFT, the smaller ones

    [1, 2, 3, 4,             5, 6, 7, 8, 9]
      maxHeap                  minHeap
    """

    def __init__(self):
        self.minHeap, self.maxHeap = [], []

    def addNum2(self, num: int) -> None:
        N, M = len(self.minHeap), len(self.maxHeap)
        if N == 0:
            heapq.heappush(self.minHeap, num)
        else:
            if num >= self.minHeap[0]:
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.maxHeap, -num)

        # balancing
        N, M = len(self.minHeap), len(self.maxHeap)
        if N > M + 1:
            smallest = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -smallest)
        elif M == N + 1:
            highest = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, highest)


    def findMedian2(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + -self.maxHeap[0]) / 2
        elif len(self.minHeap) == len(self.maxHeap) + 1:
            return self.minHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()