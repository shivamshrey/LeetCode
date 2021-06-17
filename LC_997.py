# 997. Find the Town Judge

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # if there exists no person known by all others
        # then return -1
        if len(trust) < n - 1:
            return -1
        
        in_degrees = [0] * (n + 1)
        out_degrees = [0] * (n + 1)
        
        for i, j in trust:
            out_degrees[i] += 1
            in_degrees[j] += 1
        
        for i in range(1, n + 1):
            if out_degrees[i] == 0 and in_degrees[i] == n - 1:
                return i
        
        return -1
    