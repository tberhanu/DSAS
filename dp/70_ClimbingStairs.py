class Solution:
    
    def climbStairs(self, n: int) -> int:
        """
        bottom up dp solution
                                __3rd__ (1 way to 3rd floor i.e. just stay there)
                        __2nd__(1 way to 3rd floor i.e. one step up)
                __1st__(sum of 2nd and 3rd way, just add them)
    __ground__
        """
        if n <= 2:
            return n
        N = n + 1 # to include the ground to register all distinct ways to climb
        stairs = [0] * N
        stairs[N - 1], stairs[N - 2] = 1, 1
        for i in range(N - 3, -1, -1):
            stairs[i] = stairs[i + 1] + stairs[i + 2]
        return stairs[0]
    
    def climbStairs(self, n: int) -> int:
        """
        O(1) Space Fibonacci
        
        """
        if n <= 2:
            return n

        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b

        return b
    


    def climbStairs(self, n: int) -> int:
        """
        DFS
        for n = 3
                                ground:
                    stair1                 stair2
                stair2 stair3         stair3    

        """
        i = 0 # ground
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == n or i == n - 1:
                return 1
            if i > n:
                return 0

            one_step = dfs(i + 1) # analogous to incl
            two_step = dfs(i + 2) # analogous to nincl

            memo[i] = one_step + two_step

            return memo[i]

        return dfs(i)