# 2259. Remove Digit From Number to Maximize Result
# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        result = -float('inf')
        for i in range(len(number)):
            if number[i] == digit:
                result = max(result, int(number[:i] + number[i + 1:]))
        return str(result)