# 227. Basic Calculator II

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur = 0
        last_num = 0
        prev_sign = '+' # last seen operator
        result = 0
        
        for i in range(len(s)):
            if s[i].isdigit():
                cur = cur * 10 + int(s[i])
            
            if s[i] in "+-*/" or i == len(s) - 1:
                if prev_sign == '+':
                    result += last_num
                    last_num = cur
                elif prev_sign == '-':
                    result += last_num
                    last_num = -cur
                elif prev_sign == '*':
                    last_num = last_num * cur
                elif prev_sign == '/':
                    last_num = int(last_num / cur)
                
                prev_sign = s[i]
                cur = 0
        
        result += last_num
        return result
    