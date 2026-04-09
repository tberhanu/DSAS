class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        """
        Input: nums = [1,0,1,0]
        1
        1, 0
        1, 0, 1
        1, 0, 1, 0
        
        0
        0, 1
        0, 1, 0

        1
        1, 0

        0

        [1, 0,  1,  0]
            [1, 0,  1,  0]


        [1, 0,  1,  0]
        [1, 1,  1,  1]
        [4] [3] [2] [1]
        """
        res = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] != nums[i + 1]:
                res[i] = res[i] + res[i + 1]
        return sum(res)

        # res = [1] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[j] != nums[j - 1]:
        #             res[i] += 1
        # return sum(res)          