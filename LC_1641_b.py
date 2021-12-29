# 1641. Count Sorted Vowel Strings

class Solution:
    def countVowelStrings(self, n: int) -> int:
        # dp[i] = no. of strings formed with first j vowels
        dp = [0] + [1] * 5
        
        for i in range(1, n + 1):
            for j in range(1, 6):
                dp[j] += dp[j - 1]
        
        return dp[5]
    