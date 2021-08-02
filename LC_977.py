# 977. Squares of a Sorted Array

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        
        i, j = 0, len(nums) - 1
        
        for k in range(len(nums) - 1, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                result[k] = nums[i] ** 2
                i += 1
            else:
                result[k] = nums[j] ** 2
                j -= 1
        
        return result
    