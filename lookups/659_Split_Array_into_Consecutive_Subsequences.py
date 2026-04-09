from collections import Counter, defaultdict
from typing import List, Optional

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # if nums was not sorted, make sure to sort it first so that the below code will work

        lookup_freq = Counter(nums)
        num_of_subseq_ending_at = defaultdict(int)

        for i in range(len(nums)):
            num = nums[i]

            if lookup_freq[num] == 0:
                continue
            
            if num_of_subseq_ending_at[num - 1] > 0:
                num_of_subseq_ending_at[num - 1] -= 1
                num_of_subseq_ending_at[num] += 1
                lookup_freq[num] -= 1

            elif lookup_freq[num + 1] > 0 and lookup_freq[num + 2] > 0:
                num_of_subseq_ending_at[num + 2] += 1
                lookup_freq[num + 1] -= 1
                lookup_freq[num + 2] -= 1
                lookup_freq[num] -= 1
            else:
                return False
                
        return True
            