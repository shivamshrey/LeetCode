# 1971. Find if Path Exists in Graph

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = defaultdict(list)
        
        
        # create a graph in {u1: [v1, v2, ...], u2: [v1, v3, ...]} form
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = [False] * n
        queue = collections.deque()
        
        visited[start] = True   # start is enqeued
        queue.append(start)
        
        # do a bfs traversal
        while queue:
            u = queue.popleft()
            if u == end:
                return True
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        
        return False       
                    