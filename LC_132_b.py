# 132. Palindrome Partitioning II
# https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            min_cost = float('inf')
            temp = []
            for j in range(i, n):
                temp.append(s[j])
                if temp == temp[::-1]:    # temp is palindrome
                    cost = 1 + dp[j + 1]
                    min_cost = min(min_cost, cost)
            dp[i] = min_cost

        return dp[0] - 1
    