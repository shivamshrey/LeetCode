# 1770. Maximum Score from Performing Multiplication Operations
# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

# TC: O(m^2)
# SC: O(m^2)
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        # dp[i][left] = max score gained when i operations are done, 
        #               and 'left' left numbers are used already.
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for left in range(i, -1, -1):
                right = n - 1 - (i - left)
                dp[i][left] = max(multipliers[i] * nums[left] + dp[i + 1][left + 1], # left
                                  multipliers[i] * nums[right] + dp[i + 1][left])    # right
        
        return dp[0][0]
                