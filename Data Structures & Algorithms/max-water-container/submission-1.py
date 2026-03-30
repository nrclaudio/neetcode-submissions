class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L, R = 0, len(heights) - 1
        max_area = []
        while L < R:
            left_bar = heights[L]
            right_bar = heights[R]
            area = min(left_bar, right_bar) * (R - L)
            max_area.append(area)
            if left_bar < right_bar:
                print("increase L by 1")
                L += 1
            elif left_bar > right_bar:
                print("decrease R by 1")
                R -= 1
            elif left_bar == right_bar:
                L += 1
                R -= 1
        return max(max_area)

