# 1663. Smallest String With A Given Numeric Value
# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result = ["a"] * n
        k -= n  # adjust for all the 'a' in result
        
        i = n - 1
        while k > 0:
            offset = min(25, k)     # find largest valid character
            result[i] = chr(ord("a") + offset)
            i -= 1
            k -= offset
        
        return ''.join(result)
    