# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        end up having some kind of decreasing order
        1. recurse to 2nd from the tail, save the maxx
            if val < prev saved maxx: 
        2. need to position LEFT to skip

        """

        dummy = ListNode(0, head)
        head = dummy            # very important to go one step back
        right_big_val = -math.inf
        def dfs(head):
            nonlocal right_big_val
            if head.next is None: # important
                return

            dfs(head.next)
            # HEAD just before the last node
            if head.next.val < right_big_val:
                head.next = head.next.next
            else:
                right_big_val = max(right_big_val, head.next.val)
        
        dfs(head)
        return dummy.next