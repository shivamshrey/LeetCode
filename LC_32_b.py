# 32. Longest Valid Parentheses
# https://leetcode.com/problems/longest-valid-parentheses/


# TC: O(N)
# SC: O(1)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        left, right = 0, 0
        
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            elif s[i] == ')':
                right += 1
            
            if left == right:
                max_length = max(max_length, 2 * right)
            elif right > left:
                left, right = 0, 0
        
        left, right = 0, 0
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
            elif s[i] == ')':
                right += 1
            
            if left == right:
                max_length = max(max_length, 2 * left)
            elif left > right:
                left, right = 0, 0
        
        return max_length           
                