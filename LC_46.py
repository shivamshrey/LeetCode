# 46. Permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, cur, result, n):
            if n == 0:
                result.append(list(cur))
                return
        
            for i in range(len(nums)):
                cur.append(nums[i])
                backtrack(nums[:i] + nums[i + 1:], cur, result, n - 1)
                cur.pop()
            
        result = []
        backtrack(nums, [], result, len(nums))
        return result
    