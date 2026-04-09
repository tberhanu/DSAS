class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        1. traversing from left to right, from higer degree digit to lower degree digits
            2. if we see smaller number to the right, remove the one to the left
                as long as you have the remaining K trials
        """
        stack = []
        for n in num:
            if stack == []:
                stack.append(n)
                continue
            else:
                while stack and n < stack[-1] and k > 0:
                    stack.pop()
                    k -= 1
                stack.append(n)
        if k:
            stack = stack[:-k]
            

        stack = "".join(stack).lstrip("0")
        
        return stack if stack else "0"
        
                

