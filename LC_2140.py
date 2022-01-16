# 2140. Solving Questions With Brainpower

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def solve(i):
            if i >= len(questions):
                return 0
            
            # solve
            points = questions[i][0]
            brainpower = questions[i][1]
            case_solve = solve(i + brainpower + 1)
            
            # don't solve
            case_dont_solve = solve(i + 1)
            
            return max(case_solve + points, case_dont_solve)
            
        return solve(0)
        