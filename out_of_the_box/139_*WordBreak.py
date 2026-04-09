class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        start, memo = 0, {}
        def dfs(start):
            if start in memo:
                return memo[start]

            if start >= len(s):
                memo[start] = True
                return memo[start]

            for word in wordDict:
                end = start + len(word)
                if word == s[start: end]:
                    if dfs(end):
                        memo[start] = True # Good ?
                        return True

            memo[start] = False
            return memo[start]

        return dfs(start)