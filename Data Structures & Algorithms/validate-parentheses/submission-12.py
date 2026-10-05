class Solution:
    def isValid(self, s: str) -> bool:
        valids = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = []
        for ss in s:
            if not stack:
                stack.append(ss)
            elif ss in valids.values():
                stack.append(ss)
            elif ss in valids.keys() and stack[-1] == valids[ss]:
                # current closing and previous open
                stack.pop()
            elif ss in valids.keys() and stack[-1] != valids[ss]:
                return False
        if not stack:
            return True
        else:
            return False
            