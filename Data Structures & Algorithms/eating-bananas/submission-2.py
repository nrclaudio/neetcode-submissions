import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        L, R = 1, max(piles)
        res = R # fastest rate
        while L<=R:
            M = (L + R) // 2
            k = M # rate to try
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
                
            if hours <= h: # rate  
                R = k - 1
                res = min(res, k)
            else:
                L = k + 1 # rate too slow, 
        return res        