# 797. All Paths From Source to Target

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(u, path):
            if u == len(graph) - 1:
                result.append(list(path))
                return
            
            for v in graph[u]:
                path.append(v)
                dfs(v, path)
                path.pop()
        
        result = []
        path = [0]
        dfs(0, path)
        
        return result
        