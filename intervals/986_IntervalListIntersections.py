class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        firstList = [[0,2],[5,10],[13,23],[24,25]]
            secondList = [[1,5],[8,12],[15,24],[25,26]]
        Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


        """
        result = []
        for first in firstList:
            for second in secondList:
                intersection = self.get_intersection(first, second);
                if intersection:
                    result.append(intersection)
                if second[0] > first[1]:
                    break
        return result
    
    def get_intersection(self, first, second):
        """
            --------------
                    -----------------
            --------------
        """
        
        if first[1] >= second[0] and second[1] >= first[0]: # definition of intersection
            return [max(first[0], second[0]), min(first[1], second[1])]
        return []