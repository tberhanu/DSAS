class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        t1 = "a  bcde", t2 = "a  ce" 
            1 +  t1 = "bcde", t2 = "ce"
            1 +  max(f(t1="bcde",t2="e"), f(t1="cde",t2="ce"))

        Mathematically: @ index i
        if t1[i] == t2[i]: 
            return 1 + f(t1[i+1:], t2[i+1:])
        else: 
            return max(f(t1[i:], t2[i+1:]), f(t1[i+1:], t2[i:]))
        
        this is called DP, bottom up, but we need good base case in 2D board

        """
        dp = [[0]*(len(text2)+1) for _ in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]