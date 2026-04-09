from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lefts, rights = nums[:], nums[:]
        i, j = 1, len(nums) - 2
        while i < len(nums) and j >= 0:
            lefts[i] *= lefts[i - 1]
            rights[j] *= rights[j + 1]
            i += 1
            j -= 1
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(rights[i + 1])
            elif i == len(nums) - 1:
                res.append(lefts[i - 1])
            else:
                res.append(rights[i + 1] * lefts[i - 1])
        return res