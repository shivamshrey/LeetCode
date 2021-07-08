# 394. Decode String

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] == ']':
                decoded_string = []
                # get the encoded string
                while stack[-1] != '[':
                    decoded_string.append(stack.pop())
                
                # pop '[' from stack
                stack.pop()
                base = 1
                k = 0
                # get k
                while stack and stack[-1].isdigit():
                    k = base * int(stack.pop()) + k
                    base *= 10
                
                # push decoded_string k times into the stack
                decoded_string *= k
                for ch in reversed(decoded_string):
                    stack.append(ch)
            else:
                stack.append(s[i])
                
        return ''.join(stack)
    