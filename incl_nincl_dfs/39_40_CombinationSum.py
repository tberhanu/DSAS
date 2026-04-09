from typing import List

class Solution: # 39
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result, results, i = [], [], 0

        def dfs(i, result, target):
            if target == 0:
                results.append(result[:])
                return
            if target < 0 or i >= len(candidates):
                return 

            result.append(candidates[i])
            dfs(i, result, target - candidates[i]) # incl
            result.pop()
            dfs(i+1, result, target) # nincl
        
        dfs(i, result, target)
        return results

class Solution: # 40
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        candidates = [10,1,2,7,6,1,5], target = 8
            [[1,1,6],[1,2,5],[1,7],[2,6]]
        Each number in candidates may only be used once in the combination.

        0. sort: [10,1,2,7,6,1,5]>>[1,1,2,5,6,7]
        1. incl [i], f(i+1), and 
        2. ninc, f(next_index) (next_index should have different number)
        3. base case if target == 0, or target < 0

        """
        candidates.sort()
        result, results, i = [], [], 0

        def dfs(i, result, target):
            if target == 0:
                results.append(result[:])
                return
            if target < 0 or i >= len(candidates):
                return 

            result.append(candidates[i])
            dfs(i+1, result, target - candidates[i]) # incl
            result.pop()
            next_index = self.get_next_index(i, candidates)
            if next_index != -1:
                dfs(next_index, result, target) # nincl
        
        dfs(i, result, target)
        return results

    def get_next_index(self, i, candidates):
        for j in range(i+1, len(candidates)):
            if candidates[i] != candidates[j]:
                return j
        return -1    