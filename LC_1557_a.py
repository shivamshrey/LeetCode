# 1557. Minimum Number of Vertices to Reach All Nodes

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degrees = [0] * n
        
        for u, v in edges:
            in_degrees[v] += 1
        
        result = []
        for i in range(len(in_degrees)):
            if in_degrees[i] == 0:
                result.append(i)
        
        return result
        