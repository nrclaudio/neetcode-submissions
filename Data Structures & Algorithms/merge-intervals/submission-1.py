class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        outputs = [intervals[0]]
        for start, end in intervals:
            lastEnd = outputs[-1][1]
            if start <= lastEnd:
                outputs[-1][1] = max(lastEnd, end)
            else:
                outputs.append([start, end])
        return outputs