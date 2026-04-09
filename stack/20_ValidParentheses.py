class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {")": "(", "]": "[", "}": "{"}
        stack = [s[0]]
        for symbol in s[1:]:
            if symbol in lookup.keys(): # closed
                if stack and stack[-1] == lookup[symbol]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(symbol)
        
        return len(stack) == 0
