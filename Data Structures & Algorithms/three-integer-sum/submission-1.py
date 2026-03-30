from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        results = []
        for i, n in enumerate(nums):
            re = 0 - n
            L, R = i + 1, len(nums) - 1
            while L < R:
                s = nums[L] + nums[R]
                if s == re:
                    if [n, nums[L], nums[R]] not in results:
                        results.append([n, nums[L], nums[R]])
                    L += 1
                    R -= 1
                elif s > re:
                    R -= 1
                elif s < re:
                    L += 1
        return results
