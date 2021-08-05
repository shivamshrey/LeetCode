# 78. Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(subset=[], start=0):
            result.append(copy.deepcopy(subset))
            
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(subset, i + 1)
                subset.pop()
                
        result = []
        backtrack()
        return result
        