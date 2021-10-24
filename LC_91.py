# 91. Decode Ways


class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] = max number of ways to decode string of length i
        dp = [0] * (len(s) + 1)
        dp[0] = 1  # only 1 way to decode an empty string

        # string of length 1 starting with 0 will have no mapping
        # hence no way to decode it
        # if it doesn't start with 0 then it will have 1 mapping
        # and 1 way to decode it
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2, len(s) + 1):
            last_one_digit = int(s[i - 1 : i])  # ending at i - 1
            last_two_digits = int(s[i - 2 : i])  # ending at i - 1

            if last_one_digit >= 1:
                dp[i] += dp[i - 1]

            if last_two_digits >= 10 and last_two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]
