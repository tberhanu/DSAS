class Solution:
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

