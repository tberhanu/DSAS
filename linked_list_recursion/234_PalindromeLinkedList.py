# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        left, right = head, head
        def dfs(right):
            nonlocal left
            if right is None:
                return True

            res1 = dfs(right.next)
            res2 = left.val == right.val
            
            left = left.next
            
            return res1 and res2
        
        return dfs(right)