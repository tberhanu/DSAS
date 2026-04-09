class Solution:
    def simplifyPath(self, path: str) -> str:
        paths, stack = path.split("/"), []
        for p in paths:
            if p == "." or p == "":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)

        return "/" + "/".join(stack)