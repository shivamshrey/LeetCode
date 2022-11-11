# 132. Palindrome Partitioning II
# https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        def helper(i):
            if i == n: return 0
            if dp[i] != -1: return dp[i]
            min_cost = float('inf')
            temp = []
            for j in range(i, n):
                temp.append(s[j])
                if temp == temp[::-1]:    # temp is palindrome
                    cost = 1 + helper(j + 1)
                    min_cost = min(min_cost, cost)
            dp[i] = min_cost
            return min_cost

        n = len(s)
        dp = [-1] * n
        return helper(0) - 1
    