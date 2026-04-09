from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        [1, 2, 3]
                Following inc vs ninc start "inc 1" and "ninc 1"
                                   *
                            inc  /   \ ninc
                            ([1],    [])
                    ([1, 2], [1],    [2], [])
                ([1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], [])

        """
        i, result, results = 0, [], []
        def dfs(i):
            if i >= len(nums):
                results.append(result[:])
                return

            result.append(nums[i])
            dfs(i + 1) # incl
            result.pop()
            dfs(i + 1) # nincl

        dfs(i)
        return results




























