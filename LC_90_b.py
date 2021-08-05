# 90. Subsets II

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        nums.sort()
        
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(result)
            for j in range(len(result) - l, len(result)):
                result.append(result[j] + [nums[i]])
        
        return result
    