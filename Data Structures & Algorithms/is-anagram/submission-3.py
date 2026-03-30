from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = Counter(s)
        seen_t = Counter(t)
        if seen_s == seen_t:
            return True
        else:
            return False