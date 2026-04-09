from collections import Counter, defaultdict
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        s = "ADOBECODEBANC", t = "ABC" >> "BANC"
            "ADOBEC" is 1st window, then how do you SHRINK the window effectively ?
        1. what we NEED >> need_freq = Counter(t)
        2. current freq tracker >> curr_freq = defaultdict(int)
        3. what we currently HAVE >> have += 1 (increment wisely)
           increment HAVE only if we have enough freq for specific letter in NEED
           if curr_freq[letter] == need_freq[letter]:
                have += 1
        4. how we know if we have all letters included ? >> if have == len(need_freq)
        5. how we actually shrink, move the left pointer forward: >> left = left + 1
            1. need deduct: curr_freq[s[left]] -= 1
                if curr_freq[s[left]] < need_freq[letter]: have -= 1, so right pointer continue
                else: keep shrinking
        
        """
        need_freq, curr_freq = Counter(t), defaultdict(int)
        have, need = 0, len(need_freq)
        left, right, minWindow, start, end = 0, 0, math.inf, -1, -1
        while right < len(s):
            letter = s[right]
            curr_freq[letter] += 1
            if letter in need_freq and curr_freq[letter] == need_freq[letter]:
                have += 1
            while have == need: # time to shrink
                if right - left + 1 < minWindow:
                    minWindow = right - left + 1
                    start, end = left, right
                left_letter = s[left]
                curr_freq[left_letter] -= 1
                
                if left_letter in need_freq and curr_freq[left_letter] < need_freq[left_letter]:
                    have -= 1
                left += 1
            right += 1

        return "" if minWindow == math.inf else s[start: end + 1]


        