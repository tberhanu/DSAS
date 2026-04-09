class Solution: # 670
    def maximumSwap(self, num: int) -> int:
        """
        good to replace one of the HIGHER degree digit from left, to another LOWER degree
        digit from right, as long as the one to the right is bigger than the one to the left.

        so, while traversing from left to right:
            ask: what is the biggest number I can get to the right ?
                >>> so lookup dict for INDEX is uselful

        """
        nums = list(str(num))
        lookup_index = {int(x): i for i, x in enumerate(nums)}
        
        for index, x in enumerate(nums):
            for d in range(9, int(x), -1):
                index2 = lookup_index.get(d, -1) # default value is -1, if not found
                if index2 > index:
                    nums[index2], nums[index] = nums[index], nums[index2]
                    return int("".join(nums))
        
        return num # already it's the biggest number


        