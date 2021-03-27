class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ['(', '[', '{']:
                stack.append(char)
            else:
                # stack can't be empty when a closing bracket is encountered
                if not stack:
                    return False
                elif not self.is_matching_pair(stack[-1], char):
                    return False
                else:
                    stack.pop()
        # if stack is not empty, then parantheses are not balanced
        return False if stack else True
        
    def is_matching_pair(self, a, b):
        return a == '(' and b == ')' \
            or a == '[' and b == ']' \
            or a == '{' and b == '}'
    
