# 215. Kth Largest Element in an Array

import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            p = self.partition(nums, low, high)
            if p == k - 1:
                return nums[p]
            elif p < k - 1:
                low = p + 1
            else:
                high = p - 1
        
    def partition(self, nums, low, high):
        # Using Lomuto partition scheme
        # Randomizing pivot
        rand_index = random.randint(low, high)
        nums[high], nums[rand_index] = nums[rand_index], nums[high]
        pivot = nums[high]
        i = low
        
        for j in range(low, high):
            if nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[high] = nums[high], nums[i]
        
        return i