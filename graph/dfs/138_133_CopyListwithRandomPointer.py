"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        memo = {}
        def get_copy(head):
            if head is None: 
                return head
            if head in memo:
                return memo[head]
            
            copied = Node(head.val)
            memo[head] = copied
            copied.next = get_copy(head.next)
            copied.random = get_copy(head.random)
            return copied
        return get_copy(head)
         
