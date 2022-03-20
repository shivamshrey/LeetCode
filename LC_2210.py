# 2210. Count Hills and Valleys in an Array
# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        prev = nums[0]
        
        for i in range(1, len(nums) - 1):
            if (prev < nums[i] and nums[i + 1] < nums[i]    # hill
                          or prev > nums[i] and nums[i + 1] > nums[i]): # valley
                count += 1
            prev = prev if nums[i] == nums[i + 1] else nums[i]
        
        return count
    