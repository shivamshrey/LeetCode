# 646. Maximum Length of Pair Chain
# https://leetcode.com/problems/maximum-length-of-pair-chain/

# TC: O(N^2)
# SC: O(N)

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = [1] * len(pairs)

        for j in range(len(pairs)):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)
        