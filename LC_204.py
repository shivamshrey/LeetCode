# 204. Count Primes

class Solution:
    def countPrimes(self, n: int) -> int:
        not_primes = [False] * n
        count = 0
        for i in range(2, n):
            if not not_primes[i]:
                count += 1
                j = 2
                while i * j < n:
                    not_primes[i * j] = True
                    j += 1
        
        return count
