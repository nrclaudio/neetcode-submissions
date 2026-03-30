class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sub = {}
        for i, n in enumerate(nums):
            need = target - n
            print(f"n: {n}")
            print(f"need: {need}")
            print(f"index: {i}")
            if n in sub.keys():
                return [sub[n], i]
            elif need not in sub.keys():
                sub[need] = i

            
