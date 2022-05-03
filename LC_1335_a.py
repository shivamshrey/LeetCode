# 1335. Minimum Difficulty of a Job Schedule
# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        max_difficulties = [0] * n  # max_difficulties[i] = max(jobDifficulty[i:])
        max_so_far = jobDifficulty[-1]
        for i in range(n - 1, -1, -1):
            max_so_far = max(max_so_far, jobDifficulty[i])
            max_difficulties[i] = max_so_far
        
        @functools.lru_cache(None)
        def dp(i, day):
            if n < d: return -1
            if day == d: return max_difficulties[i]
            
            result = float('inf')
            hardest = jobDifficulty[i]
            for j in range(i, n - (d - day)):
                hardest = max(hardest, jobDifficulty[j])
                result = min(result, hardest + dp(j + 1, day + 1))
            
            return result
            
        return dp(0, 1)