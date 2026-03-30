from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_table = Counter(nums).most_common(k)
        return [tup[0] for tup in frequency_table]
         

            


        