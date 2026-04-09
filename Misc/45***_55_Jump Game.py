class Solution2: # 55
    def canJump2(self, nums: List[int]) -> bool:
        target_index = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= target_index:
                target_index = i
        return target_index == 0


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable_index, i = 0, 0
        for i, num in enumerate(nums):
            if max_reachable_index < i: 
                return False
            max_reachable_index = max(max_reachable_index, i + num)

        return max_reachable_index >= len(nums) - 1
    

class Solution: # 45 ***
    def jump(self, nums: List[int]) -> int:
        # smart solution
        jumps, farthest = 0, 0
        current_end = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            # time to use another jump
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps

    def jump2(self, nums: List[int]) -> int:
        """
        nums[i] represents the maximum length of a forward jump from index i
                        [2,  3, 1, 1, 4]
                         . ->
                             . -  - ->.
        [2,      3,       1,           1,         4]
        [0,      I,       I,           I,         I] initials jump needed to reach each index
         0    min(1,I)  min(1,I)
                  1     min(2,1)     min(2,I)  min(2,I)=2 >> output => 2
        """
        # jumps_needed[i] means jumps needed to arrive index=i
        jumps_needed = [math.inf] * len(nums)
        jumps_needed[0] = 0

        for start in range(len(nums)):
            jumps = nums[start]
            for jump in range(1, jumps + 1):
                index = start + jump
                if index < len(jumps_needed):
                    jumps_needed[index] = min(jumps_needed[index], 1 + jumps_needed[start])
        return jumps_needed[-1]