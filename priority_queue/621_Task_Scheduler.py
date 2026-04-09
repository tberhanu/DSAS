from typing import List, Optional


import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        lookup_freq = Counter(tasks)
        maxHeap = []

        for letter, freq in lookup_freq.items():
            heapq.heappush(maxHeap, -freq)
        # print("maxHeap: ", maxHeap)
        queue = deque()
        count = 0

        while queue or maxHeap:
            if len(queue) == n + 1:
                freq = queue.popleft()
                if freq < 0:
                    heapq.heappush(maxHeap, (freq))
            
            if len(maxHeap) > 0:
                freq = heapq.heappop(maxHeap)
                count += 1
                queue.append(freq + 1)

            elif len(maxHeap) == 0:
                if len(queue) == 0:
                    return count
                if len(set(queue)) == 1 and queue[0] == 0:
                    return count
                else:
                    count += 1
                    queue.append(0)

        return count