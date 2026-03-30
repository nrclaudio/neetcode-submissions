class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub = {}
        for i, n in enumerate(nums):
            need = target - n
            if n in sub.keys():
                return [sub[n], i]
            elif need not in sub.keys():
                sub[need] = i

            
