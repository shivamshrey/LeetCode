# 581. Shortest Unsorted Continuous Subarray
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, end = -1, -1         # start and end of unsorted subarray
        i, j = 0, len(nums) - 1
        max_from_left, min_from_right = -float('inf'), float('inf')
        
        while i < len(nums):   # or j >= 0
            if nums[i] >= max_from_left:
                # If current number {nums[i]} is greater than {max} encountered 
                # till i, then current number {nums[i]} is the {max} till i
                max_from_left = nums[i]
            else:
                # Else current number {nums[i]} is not in sorted position
                end = i
            
            if nums[j] <= min_from_right:
                # If current number {nums[j]} is lesser than {min} encountered
                # till j, then current number {nums[j]} is the {min} till j
                min_from_right = nums[j]
            else:
                # Else current number {nums[j]} is not in sorted position
                start = j
            
            i += 1
            j -= 1
        
        # If any of the start or end is -1, then the array is sorted already, return 0.
        # else return the size of the sub array
        return end - start + 1 if start != -1 else 0            
