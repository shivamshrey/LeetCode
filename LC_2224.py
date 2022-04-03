# 2224. Minimum Number of Operations to Convert Time
# https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_in_secs = int(current[0:2]) * 60 + int(current[3:])
        correct_in_secs = int(correct[0:2]) * 60 + int(correct[3:])
        
        result = 0
        diff = correct_in_secs - current_in_secs
        
        for s in (60, 15, 5, 1):
            while diff >= s:
                diff -= s
                result += 1
        return result
        