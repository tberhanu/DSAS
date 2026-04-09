class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1]

        getting the next bigger number assuming the nums are concatenated like "123", "132", ...
        
        1. start from end, traverse backward compairing adj values
            2. when you get LEFT < RIGHT, stop!!! we know we can get the next bigger number
        3. start from end looking for num > LEFT, and stop! swap!
                3. just sort nums[LEFT + 1:]
        """
        n = len(nums)

        # 1. Find first decreasing index from the right
        index = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break

        # If no pivot found, it's the last permutation
        if index == -1:
            nums.sort()
            return

        # 2. Find the smallest number greater than nums[index] on the right
        for i in range(n - 1, index, -1):
            if nums[i] > nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
                break # here we guarantee getting Bigger num, but not the Next Bigger

        # 3. Sort the suffix, to guarantee our Bigger num to be the Next Bigger
        nums[index + 1:] = sorted(nums[index + 1:]) # possible to sort portion of the array !!!