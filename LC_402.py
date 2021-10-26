# 402. Remove K Digits

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        
        stack = []
        
        for digit in num:
            # whenever we meet a digit which is less than the previous digit, 
            # discard the previous one
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # corner case '1111' or '1234'
        if k > 0:
            stack = stack[:-k]
        
        # Strip 0s from left and return string.
        # If string becomes empty after stripping, return "0"
        return "".join(stack).lstrip("0") or "0"
    