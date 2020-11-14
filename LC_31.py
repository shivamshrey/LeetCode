# 31. Next Permutation

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i > -1:
            if nums[i] < nums[i + 1]:
                j = len(nums) - 1
                while j > i:
                    if nums[j] > nums[i]:
                        break
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                break
            i -= 1
        nums[i + 1:] = reversed(nums[i + 1:])
