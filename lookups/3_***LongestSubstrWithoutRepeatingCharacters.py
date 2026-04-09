class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        "p w w k e w"
        1. start, end
        2. track seen via lookup_index
        3. if not seen: end+=1
        4. else: shrink
            5. start = max(lookup[elt] + 1, start + 1)

        """
        start, end = 0, 0
        lookup_index, longest = {}, 0

        while end < len(s): 
            if s[end] not in lookup_index:
                lookup_index[s[end]] = end
                longest = max(longest, end - start + 1)
                end += 1
            else: # shrink
                last_seen_index = lookup_index[s[end]]
                start = max(start, last_seen_index + 1) # very tricky
                lookup_index[s[end]] = end # re-update with latest Index
                longest = max(longest, end - start + 1)
                end += 1


        return longest
