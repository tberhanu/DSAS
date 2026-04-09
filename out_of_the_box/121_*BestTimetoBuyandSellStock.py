class Solution: # smart out of the box solution
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far, max_profit = math.inf, 0
        for price in prices:
            min_price_so_far = min(min_price_so_far, price)
            max_profit = max(max_profit, price - min_price_so_far)

        return max_profit


class Solution2: # sliding window
    def maxProfit2(self, prices: List[int]) -> int:
        i, j, profit = 0, 1, 0
        while j < len(prices):

            if prices[j] >= prices[i]:
                profit = max(profit, prices[j] - prices[i])
                j += 1
            else:
                i = j # make it the buying price
                j += 1

        return profit
