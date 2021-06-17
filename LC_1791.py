# 1791. Find Center of Star Graph

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # center node will be part of every edge.
        # intersection of first 2 edges itself will be our answer
        return (set(edges[0]) & set(edges[1])).pop()
        