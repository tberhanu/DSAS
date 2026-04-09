from typing import List, Optional
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo, start = {0: 0}, 0

        def dfs(amount):
            if amount in memo:
                return memo[amount]

            if amount < 0:
                return math.inf
            
            local_min_count = math.inf

            for coin in coins:
                count = 1 + dfs(amount - coin)
                local_min_count = min(local_min_count, count)
            memo[amount] = local_min_count

            return local_min_count

        result = dfs(amount)
        return result if result != math.inf else -1


            


            

