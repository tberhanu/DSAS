# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        left_node, right_node = head, head
        done, index = False, 1
        def rec(right_node, index):
            nonlocal done, left_node
            if index == right:
                return
            if index < left:
                left_node = left_node.next
                right_node = right_node.next
                index += 1
            else:
                if index < right:
                    right_node = right_node.next
                    index += 1
                     
            
            rec(right_node, index)

            if left_node == right_node or right_node.next == left_node:
                done = True
                return
            if not done:
                left_node.val, right_node.val = right_node.val, left_node.val
                left_node = left_node.next
        
        rec(right_node, index)
        return head



class Solution2:
    def reverseBetween2(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            while head:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
            return prev
        
        dummy = ListNode(0, head)
        curr = dummy
        
        # 1. Move curr to node before 'left'
        for _ in range(left - 1):
            curr = curr.next
        
        before_left = curr
        left_node = curr.next
        
        # 2. Move curr to 'right'
        curr = left_node
        for _ in range(right - left):
            curr = curr.next
        
        right_node = curr
        after_right = curr.next
        
        # 3. Disconnect
        before_left.next = None
        right_node.next = None
        
        # 4. Reverse the sublist
        reversed_head = reverse(left_node)
        
        # 5. Reconnect
        before_left.next = reversed_head
        
        # Find tail of reversed list (original left_node)
        left_node.next = after_right
        
        return dummy.next
