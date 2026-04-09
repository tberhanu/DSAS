class Solution: # 316
    def removeDuplicateLetters(self, s: str) -> str:
        """
        1. when adding char to stack, need to check if we better use this char or other
           char coming from s in the future (if we have more of same char via last_index mapping)
            2. so, first we check previously added char is > our cur char
                3. then we need to check this prev added char is also available later (last_index)
                    4. if yes, then pop it out, keep poping out the rest of the prev added chars

        """
        last_index = {s[i]: i for i in range(len(s))}
        index, stack, seen = 1, [s[0]], {s[0]}

        for index in range(1, len(s)):
            char = s[index]
            if char in seen:
                continue
            else:
                while stack and stack[-1] > char and last_index[stack[-1]] > index:
                    seen.remove(stack.pop())
                stack.append(char)
                seen.add(char)

        return "".join(stack)

class Solution: # 402
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
        
                
class Solution: # 670
    def maximumSwap(self, num: int) -> int:
        """
        good to replace one of the HIGHER degree digit from left, to another LOWER degree
        digit from right, as long as the one to the right is bigger than the one to the left.

        so, while traversing from left to right:
            ask: what is the biggest number I can get to the right ?
                >>> so lookup dict for INDEX is uselful

        """
        nums = list(str(num))
        lookup_index = {int(x): i for i, x in enumerate(nums)}
        
        for index, x in enumerate(nums):
            for d in range(9, int(x), -1):
                index2 = lookup_index.get(d, -1) # default value is -1, if not found
                if index2 > index:
                    nums[index2], nums[index] = nums[index], nums[index2]
                    return int("".join(nums))
        
        return num # already it's the biggest number


        
