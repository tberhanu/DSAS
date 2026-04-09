class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
            count = 1
        nums = [10, 9, 2,  5, 3, 7, 101, 18]     [2,3,7,101]
                1, 1, 1,  2, 1, 
        lookup_index = {10: 0, 9: 1, ....}
        brute force:
            loop twice and update the count
            [10, 9, 2,  5, 3, 7, 101, 18] 
                [10, 9,  2,   5,    3,  7,  101,   18] 
                [1,  1,  1,   2,    2,  3,   4,    4] 

        """
        results = [1] * len(nums)
        longest = 1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    results[j] = max(results[j], results[i] + 1)
                    longest = max(longest, results[j])
        
        return longest

