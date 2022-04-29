# 785. Is Graph Bipartite?
# https://leetcode.com/problems/is-graph-bipartite/

# TC: O(N + E)
# SC: O(N)
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = dict()
        
        for u in range(len(graph)):
            if u not in color:  # for disconnect graph
                stack = [u]
                color[u] = 0
                while stack:
                    node = stack.pop()
                    for neighbor in graph[node]:
                        if neighbor not in color:
                            stack.append(neighbor)
                            color[neighbor] = color[node] ^ 1    # flip color from 0 -> 1 or 1 -> 0
                        elif color[neighbor] == color[node]:
                            return False
        return True
