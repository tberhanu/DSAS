# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2:
    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        naturally solved via BFS

        """
        if root is None:
            return []
        queue, results = deque(), [[root.val]]
        queue.append([root])
        while queue:
            nodes = queue.popleft()
            temp = []
            for node in nodes:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if temp:
                vals = [t.val for t in temp]
                results.append(vals)
                queue.append(temp)

        return results


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS
        if root is None:
            return []
        level, level_to_node = 0, defaultdict(list)
        def dfs(root, level):
            if root is None:
                return

            level_to_node[level].append(root.val)

            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        dfs(root, level)
        return list(level_to_node.values())



        