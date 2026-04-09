from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        i, total, memo = 0, 0, {}
        def dfs(i, total):
            if (i, total) in memo:
                return memo[(i, total)]
            if i == len(nums):
                if total == target:
                    return 1
                return 0
            
            pos = dfs(i+1, total + nums[i])
            neg = dfs(i+1, total - nums[i])
            memo[(i, total)] = pos + neg

            return memo[(i, total)]

        return dfs(i, total)
            
