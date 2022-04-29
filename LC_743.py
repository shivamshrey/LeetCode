# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # array to store time taken for signal to reach each node
        signal_received_at = [0] + [float('inf')] * n   # Prepend [0] due to nodes being 1 to n
        signal_received_at[k] = 0
        
        queue = collections.deque([(k, 0)])

        while queue:
            u, w = queue.popleft()
            
            if u not in graph: continue
            
            for v, w in graph[u]:
                arrival_time = signal_received_at[u] + w    # time taken from node u to v
                if signal_received_at[v] > arrival_time:
                    signal_received_at[v] = arrival_time
                    queue.append((v, arrival_time))
                    
        max_time = max(signal_received_at)
        
        # if some node is unreachable, its value will still be infinity
        return max_time if max_time != float('inf') else -1
        