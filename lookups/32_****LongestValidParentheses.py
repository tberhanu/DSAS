class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
             (     )      (     )
        -1,  0,           2,
             1--1=2            3--1=4

        "()(()"

        "( )   ( ( ) )"
           1   2 3 4 5

        """
        longest, indexes = 0, [-1]
        index = 0
        while index < len(s):
            symbol = s[index]
            if symbol == "(":
                indexes.append(index)
            else:
                indexes.pop()
                if indexes == []:
                    indexes.append(index)
                else:
                    window = index - indexes[-1]
                    longest = max(longest, window)
            index += 1
        
        return longest