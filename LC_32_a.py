# 32. Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/

# TC: O(N)
# SC: O(N)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        result = 0
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    result = max(result, i - stack[-1])
        
        return result                   
                