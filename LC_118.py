# 118. Pascal's Triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        
        for i in range(numRows - 1):
            row = []
            row.append(1)
            for j in range(len(result[-1]) - 1):
                row.append(result[-1][j] + result[-1][j + 1])
            row.append(1)
            result.append(row)
        
        return result
    