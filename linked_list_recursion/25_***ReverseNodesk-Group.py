# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        reversedHead = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return reversedHead

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count, dummy, lastNode, found = 0, head, None, False
        while head:
            count += 1
            if count == k:
                lastNode = head
                found = True
                break
            head = head.next
        if not found: # when not enough nodes of K group
            return dummy
        
        others = lastNode.next # Saving them
        lastNode.next = None # Separating nodes
        reversedNode = self.reverse(dummy)
        othersReversed = self.reverseKGroup(others, k)
        dummy.next = othersReversed

        return reversedNode