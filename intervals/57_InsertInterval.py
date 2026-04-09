class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        1. traverse
        2. if overlapped: update newInterval and continue
        3. else: insert it and break out
        corner case: check if newInterval left over not added 
        """
        result = []
        for i, interval in enumerate(intervals):
            union = self.get_union(interval, newInterval)
            if union:
                newInterval = union
            elif newInterval[0] < interval[0]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            else:
                result.append(interval)
        
        result.append(newInterval) # tricky, leftover interval to be added
        return result
    
    def get_union(self, interval, newInterval):
        if interval[0] <= newInterval[1] and newInterval[0] <= interval[1]:
            return [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]
        return []