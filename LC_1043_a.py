# 1043. Partition Array for Maximum Sum
# https://leetcode.com/problems/partition-array-for-maximum-sum/

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        def helper(i):
            if i == n: return 0
            if dp[i] != -1: return dp[i]
            max_ = float('-inf')
            length = 0
            result = float('-inf')
            for j in range(i, min(i + k, n)):
                length += 1
                max_ = max(max_, arr[j])
                result = max(result, length * max_ + helper(j + 1))
            
            dp[i] = result
            return result
        
        n = len(arr)
        dp = [-1] * n
        return helper(0)
    