# 323. Number of Connected Components in an Undirected Graph
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(i):
            visited[i] = True
            for j in graph[i]:
                if not visited[j]:
                    dfs(j)
        
        graph = [[] for _ in range(n)]
        visited = [False] * n
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)
        
        return count
    