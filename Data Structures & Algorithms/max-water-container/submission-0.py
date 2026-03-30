class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = []
        for enum_1, i in enumerate(heights):
            for enum_2, j in enumerate(heights):
                current_area = min(i, j) * (enum_2 - enum_1)
                max_area.append(current_area)
        return max(max_area)

