class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        merge sort is interesting with O(nlog(n)) time complexity

        Note: if pushing tuple to heapq, need also include uuid in the tuple in case of TIE
        # merging time
        # minHeap, merged = [], []
        # uuid = 0
        # for num in left:
        #     heapq.heappush(minHeap, (num, uuid))
        #     uuid += 1
        # for num in right:
        #     heapq.heappush(minHeap, (num, uuid))
        #     uuid += 1
        Note; We can merge via minHeap, but not efficient.
        """
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[: mid])
        right = self.sortArray(nums[mid: ])

        i, j, merged = 0, 0, []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        if i < len(left):
            merged.extend(left[i:])
        if j < len(right):
            merged.extend(right[j:])
        return merged