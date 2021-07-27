# 66. Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        
        while i >= 0 and carry == 1:
            carry, mod = divmod(digits[i] + carry, 10)
            digits[i] = mod
            i -= 1
        
        if carry == 1:
            return [carry] + digits
        
        return digits
    