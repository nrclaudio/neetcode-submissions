class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_table = Counter(nums)
        frequencies = sorted([value for value in frequency_table.values()], reverse=True)
        frequencies = frequencies[:k]
        result = []
        for key, value in frequency_table.items():
            if value in frequencies and key not in result:
                result.append(key)
        return result

            


        