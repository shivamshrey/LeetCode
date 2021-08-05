# 78. Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = list()
        self.findSubsets(nums, len(nums), [], result)
        return result
    
    def findSubsets(self, nums, n, subset, result):
        if n == 0:
            result.append(subset)
            return
        
        self.findSubsets(nums, n - 1, subset, result)
        self.findSubsets(nums, n - 1, [nums[n - 1]] + subset, result)
        