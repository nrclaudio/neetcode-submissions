class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_left = 0
        max_right = 0
        total_water = 0
        while l < r:
            if height[l] > max_left:
                max_left = height[l]
            if height[r] > max_right:
                max_right = height[r]
            if max_left < max_right:
                total_water += (max_left - height[l])
                l += 1
            elif max_right <= max_left:
                total_water += (max_right - height[r])
                r -= 1
        return total_water
        