# 1770. Maximum Score from Performing Multiplication Operations
# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

# TC: O(m^2)
# SC: O(m^2)
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @functools.lru_cache(2000)
        def dp(i, left):
            '''max score gained when i operations are done, 
            and 'left' left numbers are used already.
            '''
            if i == m: return 0
            
            right = n - 1 - (i - left)  # index of rightmost unused element
            return max(multipliers[i] * nums[left] + dp(i + 1, left + 1),   # choose from left
                       multipliers[i] * nums[right] + dp(i + 1, left))      # choose from right
        
        n, m = len(nums), len(multipliers)
        return dp(0, 0) # when 0 operations are done, 0 left numbers are used
    