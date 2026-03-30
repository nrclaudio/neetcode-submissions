class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 0
        previous = 0
        max_counter = 0
        sorted_nums = sorted(nums)
        print(sorted_nums)
        for i, num in enumerate(sorted_nums):
            diff = abs(num - previous)
            if i == 0:
                previous = num
                counter += 1
            elif diff == 0:
                previous = num
            elif i == 0:
                previous = num
                counter += 1
            elif i != 0 and diff == 1:
                previous = num
                counter += 1
            else:
                previous = num
                max_counter = counter if counter > max_counter else max_counter
                counter = 1
            print(i, num, previous, diff, counter, max_counter)
        if max_counter == 0:
            return counter
        elif max_counter < counter:
            return counter
        else:
            return max_counter


        