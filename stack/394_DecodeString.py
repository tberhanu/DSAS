class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            symbol = s[i]
            if symbol != "]":
                stack.append(symbol)
            else:
                letters = []
                while stack[-1] != "[":
                    letters.append(stack.pop())
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                letters = "".join(letters[::-1])
                decoded = int(num) * letters
                stack.append(decoded)
            i += 1
        
        return "".join(stack)


class Solution2:
    def decodeString2(self, s: str) -> str:
        """
        s is guaranteed to be a valid input.
        All the integers in s are in the range [1, 300].

        This code was meant to avoid STRING CONCATENATION as it creates brand new
        object everytime we concatenate, but also using deque() is expensive.

        Even an empty deque() is significantly heavier than a Python list.
        """
        stack = []
        for symbol in s:
            if symbol == "]":
                queue = deque()
                while stack and stack[-1] != "[":
                    queue.appendleft(stack.pop()) # appendleft
                stack.pop()
                string = "".join(queue) # .join(queue) just like .join(list)
                queue2 = deque()
                while stack and stack[-1].isdigit():
                    queue2.appendleft(stack.pop())
                number = int("".join(queue2))

                decoded = string * number
                stack.append(decoded)
            else:
                stack.append(symbol)
        
        return "".join(stack)

