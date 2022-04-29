# 1202. Smallest String With Swaps
# https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s = list(s)
        n = len(s)
        graph = collections.defaultdict(list)
        visited = [False] * n
        
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)
        
        
        for i in range(len(s)):
            if not visited[i]:
                indices = []
                chars = []
                self.dfs(i, s, chars, indices, graph, visited)
                
                chars.sort()
                indices.sort()
                for c, j in zip(chars, indices):
                    s[j] = c
        
        return "".join(s)
        
    def dfs(self, i, s, chars, indices, graph, visited):
        visited[i] = True
        indices.append(i)
        chars.append(s[i])
        
        for j in graph[i]:
            if not visited[j]:
                self.dfs(j, s, chars, indices, graph, visited)
