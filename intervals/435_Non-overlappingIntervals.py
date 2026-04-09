from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        intervals = [[1,2],[2,3],[3,4],[1,3]]
        Output: 1 since [1,3] can be removed and the rest of the intervals are non-overlapping.
        0. saved [0]
        1. sort by start time, and traverse thru [1:]
            2. if overlapped: update SAVED with the one having smaller END
            3. else: increment count, and update saved = interval
        

        """
        intervals.sort()
        saved, count = intervals[0], 0
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] < saved[1]:
                if interval[1] < saved[1]:
                    saved = interval
                count += 1
            else:
                saved = interval
        return count