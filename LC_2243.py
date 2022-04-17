# 2243. Calculate Digit Sum of a String
# https://leetcode.com/problems/calculate-digit-sum-of-a-string/

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        s = list(s)
        while len(s) > k:
            temp = []
            i = 0
            while i < len(s):
                temp.append(str(self.getSum(s[i:i + k])))
                i += k
            s = list(''.join(temp))
        return ''.join(s)
    
    def getSum(self, s: str) -> int:
        result = 0
        for d in s:
            result += int(d)
        return result