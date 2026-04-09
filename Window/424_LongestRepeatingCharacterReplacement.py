class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        1. traverse
            2. update freq map
            3. diff_letters_count = window - max_freq
            4. if diff <= k: keep going (track longest)
            5. esle: slide window, --freq, then ++start

        """
        start, end, freq, longest = 0, 0, defaultdict(int), 0
        while end < len(s):
            freq[s[end]] += 1
            window = end - start + 1
            diff_letters_count = window - max(freq.values())
            if diff_letters_count <= k:
                longest = max(longest, window)
                end += 1
            else: # slide
                freq[s[start]] -= 1
                start += 1
                end += 1 # tricky
        return longest