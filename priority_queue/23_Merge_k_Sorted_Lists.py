# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        𝑘 = number of linked lists
        𝑁 = total number of nodes across all lists
        heapify 𝑘 linked lists: O(𝑘)
        push and pop from the min-heap 𝑁 times: O(𝑁 log 𝑘)
        Overall time complexity: O(𝑁 log 𝑘)
        Space complexity: 
            lists array takes O(𝑘) space, 
            min-heap can grow up to O(𝑘) in size, 
            and the output linked list takes O(𝑁) space. 
            Overall space complexity: O(𝑁 + 𝑘)
        """
        minHeap = []
        for i, llst in enumerate(lists):
            if llst:
                heapq.heappush(minHeap, (llst.val, i, llst))
        if not minHeap:
            return None

        node = ListNode()
        dummy = node

        while minHeap:
            val, i, llst = heapq.heappop(minHeap)
            node.next = ListNode(val)
            node = node.next
            if llst.next:
                heapq.heappush(minHeap, (llst.next.val, i, llst.next))

        return dummy.next
    
if __name__ == "__main__":
    lists = [[1,4,5],[1,3,4],[2,6]]
    lists = [ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]
    solution = Solution()
    ll = solution.mergeKLists(lists)
    arr = []
    while ll:
        arr.append(ll.val)
        ll = ll.next
    print(arr)