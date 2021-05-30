# 202. Happy Number

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n > 1 and n not in seen:
            seen.add(n)
            result = 0
            while n > 0:
                result += (n % 10) ** 2
                n //= 10
            n = result
        
        return n == 1
    