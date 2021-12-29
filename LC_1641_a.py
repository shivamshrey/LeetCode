# 1641. Count Sorted Vowel Strings

class Solution:
    def countVowelStrings(self, n: int) -> int:
        # dp[i][j] = no. of strings of length i formed with first j vowels
        dp = [[0] * 6 for _ in range(n + 1)]
        
        for i in range(n + 1):
            for j in range(1, 6):
                if i == 0:
                    dp[i][j] = 1
                elif j == 0:
                    dp[i][0] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[-1][-1]
    