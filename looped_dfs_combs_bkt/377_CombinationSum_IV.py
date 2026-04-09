from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        this question has permutation embedded as both (1, 1, 2) & (1, 2, 1) counted
        nums = [1,2,3], target = 4
        (1, 1, 1, 1),(1, 1, 2),(1, 2, 1),(1, 3),(2, 1, 1),(2, 2),(3, 1) >> 7

         NOTE: if using incl rec call under the loop, you don't need to have nincl rec call,
              as the next iteration is technically the nincl rec call

        NOTE: if decide to rec call under the loop, need to have a local variable just above the loop

        """
        memo = {}
        def dfs(target):
            if target in memo:
                return memo[target]
            if target == 0:
                return 1
            if target < 0:
                return 0

            count = 0
            for num in nums:
                count += dfs(target - num) # incl
                # nincl not needed if rec call under for loop as the next iteration is 
                # technically the nincl rec call
            memo[target] = count
            return memo[target]

        return dfs(target)
            
