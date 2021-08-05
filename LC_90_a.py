# 90. Subsets II

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(subset=[], start=0):
            result.append(copy.deepcopy(subset))
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                backtrack(subset, i + 1)
                subset.pop()
                
        result = []
        nums.sort()
        backtrack()
        return result
    