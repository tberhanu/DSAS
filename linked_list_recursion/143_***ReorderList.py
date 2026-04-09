# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        left, stop = head, False

        def rec(right):
            nonlocal left, stop
            if not right:
                return

            rec(right.next)

            if stop: # Great
                return

            if left is right or left.next is right:
                right.next = None
                stop = True
                return

            saved = left.next
            left.next = right
            right.next = saved
            left = saved

        rec(head)





class Solution2:
    def reorderList2(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.


        0. we have LEFT as nonlocal, and HEAD via recursion
        1. traverse to the tail node, last node.
        2. save the left.next for later: SAVED
            3. then point left.next to the last nose
                4. and last node to point to the SAVED left.next at #2
        5. Prep for the next backtrack of recursion call:
            - point left to the SAVED
            - the head will naturally back from tail to the prev node
        6. handle the tricky corner cases to stop swapping.
        """
        dummy = ListNode(0, head)
        left, keep_swapping = head, True
        def rec(head):
            nonlocal left, keep_swapping
            if head is None:
                return
            
            rec(head.next)
            # now HEAD is at the LAST node
            if keep_swapping:
                if left == head: # tricky corner case
                    head.next = None
                    keep_swapping = False
                else:
                    saved = left.next
                    left.next = head
                    if head != saved:
                        head.next = saved
                    else: # tricky corner case
                        head.next = None 
                        keep_swapping = False
                    left = saved
        rec(head)
        return dummy.next

            
        