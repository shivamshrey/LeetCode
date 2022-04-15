# 427. Construct Quad Tree
# https://leetcode.com/problems/construct-quad-tree/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        if not grid: return None
        if self.isLeaf(grid):
            return Node(grid[0][0] == 1, True, None, None, None, None)
        n = len(grid)
        return Node(False,  # can be True too, doesn't matter
                    False,
                    self.construct([row[:n // 2] for row in grid[:n // 2]]), # topleft
                    self.construct([row[n // 2:] for row in grid[:n // 2]]), # topright
                    self.construct([row[:n // 2] for row in grid[n // 2:]]), # bottomleft
                    self.construct([row[n // 2:] for row in grid[n // 2:]])) # bottomright
    
    def isLeaf(self, grid):
        return all(grid[0][0] == grid[i][j]
                   for i in range(len(grid))
                   for j in range(len(grid[i])))
    