# 967. Numbers With Same Consecutive Differences
# https://leetcode.com/problems/numbers-with-same-consecutive-differences/

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def dfs(num, n):
            if n == 0:
                result.append(num)
            else:
                tail_digit = num % 10
                if tail_digit - k >= 0:
                    dfs(num * 10 + tail_digit - k, n - 1)
                if k != 0 and tail_digit + k <= 9:
                    dfs(num * 10 + tail_digit + k, n - 1)
        
        result = list()
        for num in range(1, 10):
            dfs(num, n - 1)
        return result