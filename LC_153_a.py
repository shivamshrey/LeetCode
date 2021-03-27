# 153. Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = int(low + (high - low) / 2)
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[low] <= nums[mid] and nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        
        return nums[low]
