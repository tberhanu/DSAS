from typing import List


class Solution: # 78 DFS
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
    

from typing import List

class Solution: # 78 Loop
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        nums = [1,2,3]
        [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
        0. have results = [[]]
        1. traverse thru nums
            2. loop range(N) where N = len(results)
                3. for each elt in results, append num

        Note: python objects passed by reference, so need to copy not to alter
        arr = [2, [5]]
        a = 2, a += 3 # this won't alter arr >> [2, [5]]
        b = arr[1], b.appen(6) # this will alter arr >> [2, [5, 6]]

        """
        results = [[]]
        for num in nums:
            N = len(results)
            for i in range(N):
                temp = results[i][:] # shallow copy, otherwise will alter the original
                temp.append(num)
                results.append(temp)

        return results

# 90 subsets II
from typing import List

class Solution: # 90
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



from typing import List

class Solution: # 90
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        nums = [1,2,2]
        [[],[1],[1,2],[1,2,2],[2],[2,2]]
        * Subsets Loop with some change to avoid dedups
        1. sort nums
        2. have results = [[]]
        3. track the index: start, end = 0, len(results)
        4. if [i] == [i-1]: loop over range(start, end, 1)
        5. else: loop over range(0, end, 1)
        
        Trick: prev hold the index of the previous end index, so if same number appear,
               you don't start from index=0, instead from prev which avoid dups
        """
        nums.sort()
        N, results = 0, [[]]
        for i, num in enumerate(nums):
            prev, N = N, len(results)
            if i != 0 and nums[i] == nums[i - 1]:
                start = prev
            else:
                start = 0
            for j in range(start, N, 1):
                temp = results[j][:] # shallow copy
                temp.append(num)
                results.append(temp)
        return results