class Solution:
    def isValid(self, s: str) -> bool:
        valids = {"}": "{",
        ")": "(",
        "]": "["}
        stack = []
        for char in s:
            if char in valids.values(): #opening
                stack.append(char)
            elif char in valids.keys() and stack: #closing
                if stack[-1] == valids[char]: # closing and the last one matches
                    stack.pop()
                elif stack[-1] != valids[char]:
                    return False
            else:
                return False
        if stack:
            return False
        else:
            return True
            
            
        
