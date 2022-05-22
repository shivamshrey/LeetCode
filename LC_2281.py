# 2281. Sum of Total Strength of Wizards
# https://leetcode.com/problems/sum-of-total-strength-of-wizards/

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(strength)
        
        # next small on the right
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] > strength[i]:
                right[stack.pop()] = i
            stack.append(i)

        # next small on the left
        left = [-1] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and strength[stack[-1]] >= strength[i]:
                left[stack.pop()] = i
            stack.append(i)

        # for each strength[i] as minimum, calculate sum
        res = 0
        acc = list(accumulate(accumulate(strength), initial = 0))
        for i in range(n):
            l, r = left[i], right[i]
            lacc = acc[i] - acc[max(l, 0)]
            racc = acc[r] - acc[i]
            ln, rn = i - l, r - i
            res += strength[i] * (racc * ln - lacc * rn)
        return res % mod