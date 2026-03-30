class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for number in nums:
            if number not in my_dict:
                my_dict[number] = 1
            else:
                my_dict[number] += 1
                return True
        return False
         