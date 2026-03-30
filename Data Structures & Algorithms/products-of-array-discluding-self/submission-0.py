class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        reversed_nums = [i for i in reversed(nums)]
        prefix_prod = 1
        prefix = []
        postfix_prod = 1
        postfix = []
        length = len(nums) - 1
        for i, num in enumerate(nums):
            if i == 0:
                prefix.append(1)
            else:
                prefix_prod *= nums[i-1]
                prefix.append(prefix_prod)
        for i, num in enumerate(reversed_nums):
            if i == 0:
                postfix.append(1)
            else:
                postfix_prod *= reversed_nums[i-1]
                postfix.append(postfix_prod)
        postfix = [i for i in reversed(postfix)]
        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * postfix[i])    
        return result