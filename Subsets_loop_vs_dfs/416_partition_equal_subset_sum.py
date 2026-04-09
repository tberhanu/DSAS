class Solution: # Out of the Box 
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: return False
        target = sum(nums) // 2

        subsets = set()
        subsets.add(0)

        for num in nums:
            if target - num in subsets:
                return True
            lst = list(subsets) # copying is important as we can't index set
            for s in lst:
                subsets.add(num + s)
            subsets.add(num)
        
        return False



class Solution2:
    def canPartition2(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0: return False

        target, i, memo = sum(nums) // 2, 0, {}
        def dfs(i, target):
            if (i, target) in memo:
                return memo[(i, target)]
            if target == 0:
                return True
            if target < 0 or i >= len(nums):
                return False

            incl = dfs(i + 1, target - nums[i])
            ninc = False
            if not incl:
                ninc = dfs(i + 1, target)
            memo[(i, target)] = incl or ninc

            return memo[(i, target)]
        return dfs(i, target)
