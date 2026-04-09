# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """

        1. traverse both, add and make Node
        2. carry if add is >= 10 >> carry
        """
        dummy = head = ListNode()
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = val1 + val2 + carry
            digit = val % 10
            carry = val // 10
            head.next = ListNode(digit)
            head = head.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next