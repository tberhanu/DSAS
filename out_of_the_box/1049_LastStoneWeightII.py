class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) // 2 # Very Tricky, Watch Out !!! Gives us the Floor, not Ceil
        i, total, memo = 0, 0, {}

        def dfs(i, total):
            if (i, total) in memo:
                return memo[(i, total)]
            if i == len(stones):
                if total <= target: # Important
                    return total
                return -math.inf


            incl = dfs(i + 1, total + stones[i])
            ninc = dfs(i + 1, total)

            memo[(i, total)] = max(incl, ninc) # need the max num just <= target
            return memo[(i, total)]

        val1 = dfs(i, total) # gives the min num just bigger than the target
        val2 = sum(stones) - val1 # getting the other sum
        diff = val2 - val1 # val2 >= val1
        return diff