class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        L, R = 0, len(s) - 1
        while L < R:
            if not s[L].isalnum():
                L += 1
            elif not s[R].isalnum():
                R -= 1
            elif s[L] == s[R]:
                L += 1
                R -= 1
            elif s[L] != s[R]:
                return False
            elif L > R:
                return False
        return True
        