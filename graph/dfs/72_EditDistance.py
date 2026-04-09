from typing import List, Optional

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        word1 = "horse",                      word2 = "ros"
             if same: (i+1,j+1)
             if diff: insert:   (i, j+1)
                      delete:   (i+1, j)
                      replace:  (i+1, i+1)
        """
        i, j, memo = 0, 0, {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= len(word1): # tricky base case
                return len(word2[j:])
            if j >= len(word2): # tricky base case
                return len(word1[i:])

            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i+1, j+1)
            else:
                insert = 1 + dfs(i, j+1)
                delete = 1 + dfs(i+1, j)
                replace = 1 + dfs(i+1, j+1)
                memo[(i, j)] = min(insert, delete, replace)
            
            return memo[(i, j)]
        
        return dfs(i, j)