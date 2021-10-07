# 77. Combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(result, cur, n, k, start):
            if k == 0:
                result.append(list(cur))
                return
            
            for i in range(start, n + 1):
                cur.append(i)
                backtrack(result, cur, n, k - 1, i + 1)
                cur.pop()
        
        result = []
        backtrack(result, [], n, k, 1)
        return result
    