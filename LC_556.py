# 556. Next Greater Element III
# https://leetcode.com/problems/next-greater-element-iii/

# TC: O(n)
# SC: O(digits(n))

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 2
        while i > -1:
            if digits[i] < digits[i + 1]:
                j = len(digits) - 1
                while i < j and digits[i] >= digits[j]: j -= 1
                digits[i], digits[j] = digits[j], digits[i]
                break
            i -= 1
        digits[i + 1:] = reversed(digits[i + 1:])
        
        num = int(''.join(digits))
        
        if i < 0 or num < n or num >= (1 << 31): return -1      
        
        return num
    