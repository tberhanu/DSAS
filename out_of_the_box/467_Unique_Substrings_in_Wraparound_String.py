
from collections import defaultdict


class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        """
        "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

        s = "zab".  >>>> ("z", "a", "b", "za", "ab", and "zab")
        
        """
        longest, countEndingAt = 1, defaultdict(int)
        countEndingAt[s[0]] = 1 # str key (not int index) to maintain uniqueness
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i - 1]) == 1 or s[i - 1: i + 1] == "za":
                longest += 1
            else:
                longest = 1
            countEndingAt[s[i]] = max(countEndingAt[s[i]], longest) # removes dedups count, (dict key, s[i])

            
        return sum(countEndingAt.values())


