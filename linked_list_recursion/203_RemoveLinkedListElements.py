Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution2:
    def removeElements2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        if found val: h.next = h.next.next

        """
        if head is None: return None
        dummy = ListNode(0, head) 
        head = dummy # pulling HEAD one step back 
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return dummy.next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        head = dummy
        def rec(head, val):
            if head is None or head.next is None:
                return
            
            if head.next.val == val:
                head.next = head.next.next # skipping the NEXT node
                rec(head, val) # again, let's try again while standing at the same HEAD
            else:
                rec(head.next, val)
        rec(head, val)
        return dummy.next