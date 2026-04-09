from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        NOTE: This one isn't fancy, but more clear !!!
        1. maxHeap by freq
            2. heappop and add to result
            3. also add to queue
            4. if len(queue) == 2: pop from queue and push to maxHeap
        5. how to know if completed successfully: len(result) == len(s)

        """
        result, queue = [], deque()
        lookup_freq, maxHeap = Counter(s), []

        for letter, freq in lookup_freq.items():
            heapq.heappush(maxHeap, (-freq, letter))

        while maxHeap or len(queue) == 2:
            if len(queue) == 2:
                freq, letter = queue.popleft()
                if freq != 0: # then check if freq is Not Zero here
                    heapq.heappush(maxHeap, (freq, letter))

            if maxHeap:      
                freq, letter = heapq.heappop(maxHeap)
                result.append(letter)
                # Tricky: Add to Queue even if freq+1 is Zero as to count the cool off period
                queue.append((freq + 1, letter)) 
            
        if queue and queue[0][0] != 0:
            return ""
        return "".join(result)

        
    def reorganizeString2(self, s: str) -> str:
        """
        NOTE: This works fine, but too tricky and confusing as commented below !!!
        1. maxHeap by freq
            2. heappop and add to result
            3. also add to queue
            4. if len(queue) == 2: pop from queue and push to maxHeap
        5. how to know if completed successfully: len(result) == len(s)

        """
        result, queue = [], deque()
        lookup_freq, maxHeap = Counter(s), []

        for letter, freq in lookup_freq.items():
            heapq.heappush(maxHeap, (-freq, letter))

        while maxHeap:
            freq, letter = heapq.heappop(maxHeap)
            result.append(letter)
            freq += 1
            # Tricky: Add to Queue even if freq is Zero as to count the cool off period
            queue.append((freq, letter)) 
            if len(queue) == 2:
                freq, letter = queue.popleft()
                if freq != 0: # then check if freq is Not Zero here
                    heapq.heappush(maxHeap, (freq, letter))

        return "".join(result) if len(result) == len(s) else ""

        