# 1043. Partition Array for Maximum Sum
# https://leetcode.com/problems/partition-array-for-maximum-sum/

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            length = 0
            max_ = float('-inf')
            result = float('-inf')
            for j in range(i, min(i + k, n)):
                length += 1
                max_ = max(max_, arr[j])
                result = max(result, length * max_ + dp[j + 1])
            dp[i] = result
        return dp[0]
    