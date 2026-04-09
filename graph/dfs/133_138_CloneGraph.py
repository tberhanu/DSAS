"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        memo = {}
        def get_clone(node):
            if node is None:
                return None
            if node in memo:
                return memo[node]
            
            cloned = Node(node.val)
            memo[node] = cloned

            for nei in node.neighbors:
                cloned_nei = get_clone(nei)
                cloned.neighbors.append(cloned_nei)

            return cloned
        return get_clone(node)