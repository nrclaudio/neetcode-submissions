class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
    
        while left <= right:
            mid = (left + right) // 2
            
            # Check if we found the target
            if nums[mid] == target:
                return mid
                
            # Determine which half is properly sorted
            if nums[left] <= nums[mid]:
                # The left half is sorted
                if nums[left] <= target < nums[mid]:
                    # Target is in the left half
                    right = mid - 1
                else:
                    # Target is in the right half
                    left = mid + 1
            else:
                # The right half is sorted
                if nums[mid] < target <= nums[right]:
                    # Target is in the right half
                    left = mid + 1
                else:
                    # Target is in the left half
                    right = mid - 1
                    
        return -1