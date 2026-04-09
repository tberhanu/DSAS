from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        [[1,6],[8,10],[15,18]]
        * sort by starting time
        0. saved [0]
        1. traverse thru [1:]
            2. if overlap with saved, saved = merge(saved, elt)
            3. else: add saved to results, and saved = elt
        4. tricky: after exiting loop, add leftover saved to results

        """
        intervals.sort(key=lambda x: x[0]) # intervals.sort() also works
        saved, results = intervals[0], []

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= saved[1]:
                saved = [saved[0], max(saved[1], interval[1])]
            else:
                results.append(saved)
                saved = interval
        
        results.append(saved)
        return results

