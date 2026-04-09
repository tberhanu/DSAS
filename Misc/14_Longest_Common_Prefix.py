from typing import List, Optional


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """

        strs = ["fl ower","fl ow","fl ight"]
        ['flow', 'flower', 'flight']

        """

        strs.sort(key=lambda s: len(s))
        # print(strs)

        for i, char in enumerate(strs[0]): # flow
            for letter in strs[1:]: # ['flower', 'flight']
                if letter[i] != char:
                    return strs[0][: i]
        
        return strs[0]
        