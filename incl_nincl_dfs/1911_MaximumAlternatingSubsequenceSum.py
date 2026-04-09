
from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        """
                            [4,2,5,3], fl=1
        incl = fl*(4), f(2,5,3))             nincl = f(2,5,3),fl=1
        -f*(2),f(5,3)                           fl*(2), f(5,3)

        """

        i, flag, memo = 0, 1, {}
        def dfs(i, flag):
            if (i, flag) in memo:
                return memo[(i, flag)]
            if i == len(nums):
                return 0

            incl = flag*nums[i] + dfs(i+1, -flag)
            ninc = dfs(i+1, flag)
            memo[(i, flag)] = max(incl, ninc)
            
            return memo[(i, flag)]
        
        return dfs(i, flag)

