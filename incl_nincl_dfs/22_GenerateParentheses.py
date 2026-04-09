from typing import List
# Not typically incl vs nincl, but similar idea
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        opened, closed, result, results = 0, 0, [], []

        def dfs(opened, closed, result):
            if opened == closed == n:
                results.append("".join(result))
                return
            if opened > n or closed > n:
                return

            result.append("(")
            dfs(opened + 1, closed, result)
            result.pop()
            if closed < opened:
                result.append(")")
                dfs(opened, closed + 1, result)
                result.pop()
        
        dfs(opened, closed, result)
        return results