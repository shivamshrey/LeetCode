# 189. Rotate Array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse_in_range(nums, 0, n - 1)
        self.reverse_in_range(nums, 0, k - 1)
        self.reverse_in_range(nums, k, n - 1)
        
    def reverse_in_range(self, nums: List[int], i: int, j: int) -> None:
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
            