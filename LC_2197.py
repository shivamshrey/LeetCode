# 2197. Replace Non-Coprime Numbers in Array
# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        lcm = lambda x, y : x * y // math.gcd(x, y)
        stack = []
        for num in nums:
            stack.append(num)
            while len(stack) >= 2 and math.gcd(stack[-1], stack[-2]) > 1:
                stack.append(lcm(stack.pop(), stack.pop()))
                
        return stack
