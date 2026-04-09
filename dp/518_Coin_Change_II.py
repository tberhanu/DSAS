class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]

        return dp[amount]


class Solution2: # Time Limit Exceeded    29 / 31 testcases passed
    def change(self, amount: int, coins: List[int]) -> int:
        start, memo = 0, {}
        def dfs(amount, start):
            if (amount, start) in memo:
                return memo[(amount, start)]

            if start >= len(coins):
                return 0
            if amount == 0:
                return 1
            if amount < 0:
                return 0


            local_comb_counts = 0

            for index in range(start, len(coins)):
                count = dfs(amount - coins[index], index)
                local_comb_counts += count

            memo[(amount, start)] = local_comb_counts

            return local_comb_counts
        
        res = dfs(amount, start)
        return res

