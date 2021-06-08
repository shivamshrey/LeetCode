# 283. Move Zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums):
            while i < len(nums) and nums[i] != 0:
                i += 1
            j = i + 1
            while j < len(nums) and nums[j] == 0:
                j += 1
            if j >= len(nums):
                break
            nums[i], nums[j] = nums[j], nums[i]
        