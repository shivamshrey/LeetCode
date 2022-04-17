# 2244. Minimum Rounds to Complete All Tasks
# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks.sort()
        result = 0
        i = 0
        while i < len(tasks):
            j = i
            while i < len(tasks) and tasks[i] == tasks[j]: i += 1
            
            if i - j == 1: return -1
            result += (i - j + 2) // 3
        
        return result