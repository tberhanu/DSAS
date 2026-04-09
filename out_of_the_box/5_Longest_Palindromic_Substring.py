class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        s = "b a b a d"
    index    0 1 2 3 4
    num_of_pal_centered at index: 0, 1, 2 ...

        """
        index, N = 0, len(s)
        start, end = 0, 0
        while index < N:
            # ODD
            left, right = index, index
            while left >= 0 and right < N and s[left] == s[right]:
                if right - left > end - start:
                    start, end = left, right
                left -= 1
                right += 1

            # EVEN
            left, right = index, index + 1
            while left >= 0 and right < N and s[left] == s[right]:
                if right - left > end - start:
                    start, end = left, right
                left -= 1
                right += 1
            index += 1
        return s[start: end + 1]