# 1416. Restore The Array
# https://leetcode.com/problems/restore-the-array/description/

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        memo = [0] * len(s) + [1]

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0': continue
            count = 0
            for j in range(i, len(s)):
                if int(s[i:j + 1]) > k: break
                count += memo[j + 1]
            memo[i] = count % (10 ** 9 + 7)
        return memo[0]
