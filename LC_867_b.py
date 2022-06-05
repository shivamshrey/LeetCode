# 867. Transpose Matrix
# https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return zip(*matrix)
        