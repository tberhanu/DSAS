from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        sort it to jump the next NUM if similar to prev NUM to dedup

        NOTE: if using incl recursive call under the loop, you don't need to have nincl recursive call,
              as the loop will take care of it by jumping to the next index with different number

        """
        nums.sort()
        
        index, result, results = 0, [], []
        def dfs(index, result):
            
            results.append(result[:])
            
            while index < len(nums):
                result.append(nums[index])
                dfs(index + 1, result) # incl only, not nincl as recursive call under the loop
                result.pop()
                index = getNextIndex(nums, index)

        dfs(index, result)
        return results

def getNextIndex(nums, i):
    for j in range(i + 1, len(nums)):
        if nums[j] != nums[i]:
            return j
    return len(nums)