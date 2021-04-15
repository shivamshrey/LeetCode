# 268. Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
            
        for num in range(0, len(nums) + 1):
            res ^= num
        
        return res
