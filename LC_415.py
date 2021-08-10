# 415. Add Strings

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        queue = collections.deque()
        num1 = list(num1)
        num2 = list(num2)
        carry = 0
        
        while num1 or num2:
            n1 = ord(num1.pop()) - ord("0") if num1 else 0
            n2 = ord(num2.pop()) - ord("0") if num2 else 0
            
            carry, digit = divmod(n1 + n2 + carry, 10)
            queue.appendleft(digit)
        
        if carry:
            queue.appendleft(carry)
        
        return ''.join(str(i) for i in queue)
    