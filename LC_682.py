# 682. Baseball Game

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score = []
        
        for ch in ops:
            if ch == '+':
                score.append(score[-1] + score[-2])
            elif ch == 'D':
                score.append(score[-1] * 2)
            elif ch == 'C':
                score.pop()
            else:
                score.append(int(ch))
        
        result = 0
        while score:
            result += score.pop()
        
        return result
    