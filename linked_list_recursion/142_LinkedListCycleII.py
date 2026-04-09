# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head # unlike get_mid's: slow,fast=head,head.next
        found = False
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                found = True
                break

        if not found:
            return None

        while True:
            if head == slow:
                return head
            head = head.next
            slow = slow.next