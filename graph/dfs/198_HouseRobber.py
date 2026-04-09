from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int: # DP
        """
        a, b = nums[0], nums[1]
        c=(c+a, b), d=(d+b, c)

        [2, 1,  1,    2]
        [2, 1, (3,1), (3,2]
        """
        if len(nums) <= 2:
            return max(nums)

        dp = nums[:]
        dp[1] = max(dp[0], dp[1]) # important, dp[0] and dp[1], the start of our dp
        for index in range(2, len(nums)):
            incl = nums[index] + dp[index - 2] # tricky: nums vs dp
            ninc = dp[index - 1]
            dp[index] = max(incl, ninc)

        return dp[-1]        



    def rob2(self, nums: List[int]) -> int: # DFS
        """
                         [1,2,3,1], i=0
                max(f(1, i=i+2),  f(0, i=i+1))

        """
        amt, i, memo = 0, 0, {}
        def dfs(amt, i):
            if (amt, i) in memo:
                return memo[(amt, i)]
            if i >= len(nums):
                return amt

            incl = dfs(amt + nums[i], i + 2)
            ninc = dfs(amt, i + 1)

            memo[(amt, i)] = max(incl, ninc)

            return memo[(amt, i)]

        return dfs(amt, i)