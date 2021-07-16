# 227. Basic Calculator II

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur = 0
        prev_sign = '+' # last seen operator
        
        for i in range(len(s)):
            if s[i].isdigit():
                cur = cur * 10 + int(s[i])
            
            if s[i] in "+-*/" or i == len(s) - 1:
                if prev_sign == '+':
                    stack.append(cur)
                elif prev_sign == '-':
                    stack.append(-cur)
                elif prev_sign == '*':
                    stack.append(stack.pop() * cur)
                elif prev_sign == '/':
                    stack.append(int(stack.pop() / cur))
                
                prev_sign = s[i]
                cur = 0
                
        return sum(stack)
    