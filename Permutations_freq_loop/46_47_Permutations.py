from collections import Counter
from typing import List

# 46 and 47 have same solution

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        frequency = Counter(nums)
        result, results = [], []

        def dfs():
            if len(result) == len(nums):
                results.append(result[:])
                return
            for num, freq in frequency.items(): # secret is looping over the freq
                if freq > 0:
                    result.append(num)
                    frequency[num] -= 1

                    dfs()

                    result.pop()
                    frequency[num] += 1

        dfs()
        return results
    
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        frequency = Counter(nums)
        result, results = [], []

        def dfs():
            if len(result) == len(nums):
                results.append(result[:])
                return
            for num, freq in frequency.items(): # secret is looping over the freq
                if freq > 0:
                    result.append(num)
                    frequency[num] -= 1

                    dfs()

                    result.pop()
                    frequency[num] += 1

        dfs()
        return results

    