# 1557. Minimum Number of Vertices to Reach All Nodes

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return list(set(range(n)) - set(v for u, v in edges))
        