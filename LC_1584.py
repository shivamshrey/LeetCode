# 1584. Min Cost to Connect All Points
# https://leetcode.com/problems/min-cost-to-connect-all-points/

# TC: O(N⋅(N+N))=O(N^2)
# SC: O(N+N)=O(N)
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_distance = [float('inf')] * n
        min_distance[0] = 0
        mst = [False] * n
        result = 0
        edges_used = 0
        manhattan = lambda point1, point2: abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        while edges_used < n:
            u = -1
            for i in range(n):
                if not mst[i] and (u == -1 or min_distance[i] < min_distance[u]):
                    u = i
            
            mst[u] = True
            edges_used += 1
            result += min_distance[u]
            
            for v in range(n):
                distance = manhattan(points[u], points[v])
                if not mst[v] and u != v:
                    min_distance[v] = min(min_distance[v], distance)
        
        return result