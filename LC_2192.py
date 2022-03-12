# 2192. All Ancestors of a Node in a Directed Acyclic Graph
# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

# TC: O(n ^ 2)
# SC: O(n ^ 2)
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def dfs(u, v):
            for i in adj_list[v]:
                if ancestors[i] and ancestors[i][-1] == u: continue
                ancestors[i].append(u)
                dfs(u, i)
            
            
        adj_list = defaultdict(list)
        ancestors = [[] for _ in range(n)]
        
        for u, v in edges:
            adj_list[u].append(v)
            
        for u in range(n):
            dfs(u, u)
        
        return ancestors          
        