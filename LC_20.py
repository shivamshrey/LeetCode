class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in "{[(":
                stack.append(char)
            elif not stack or not self.__isMatch(stack.pop(), char):
                    return False
        
        return not stack
        
    def __isMatch(self, a, b):
        return a == '(' and b == ')' \
            or a == '[' and b == ']' \
            or a == '{' and b == '}'
    
