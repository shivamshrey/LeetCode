# 456. 132 Pattern
# https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        s3 = -float('inf')
        for s1 in reversed(nums):
            if s1 < s3:
                return True
            else:
                while stack and s1 > stack[-1]:
                    s3 = stack.pop()
            stack.append(s1)
        
        return False
        