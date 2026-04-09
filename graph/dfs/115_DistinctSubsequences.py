class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        s = "rabb bit", t = "rabb it"
        bottom up dp not working for this problem
        N = len(s), M = len(t)
        time complexity:
        without memoization: O(2^N) because we have 2 choices at each index of s, include or not include
        with memoization: O(N*M) because we have N*M unique states in our memoization table

        space complexity without memoization: O(N) for call stack
        space complexity: O(N*M) for memoization
        
        Better space without memo but still much faster with memoization
        """
        i, j, memo = 0, 0, {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == len(t): return 1
            if i == len(s): return 0

            if s[i] == t[j]:
                incl = dfs(i+1, j+1)
                ninc = dfs(i+1, j)
            else:
                incl = 0
                ninc = dfs(i+1, j)

            memo[(i, j)] = incl + ninc
            return memo[(i, j)]


        return dfs(i, j)
        

