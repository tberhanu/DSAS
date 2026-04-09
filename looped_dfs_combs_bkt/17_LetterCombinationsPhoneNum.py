
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lookup = {'2': 'abc','3': 'def','4': 'ghi','5': 'jkl',
                  '6': 'mno','7': 'pqrs','8': 'tuv','9': 'wxyz'}

        index, comb, combs = 0, [], []
        def dfs(index, comb):
            if index == len(digits):
                combs.append("".join(comb[:]))
                return

            letters = lookup[digits[index]]
            for letter in letters:
                comb.append(letter)
                dfs(index+1, comb)
                comb.pop()

        dfs(index, comb)
        return combs
