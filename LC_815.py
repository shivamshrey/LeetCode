# 815. Bus Routes
# https://leetcode.com/problems/bus-routes/

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        queue = collections.deque() # stops
        visited_buses = set()
        visited_stops = set()
        graph = collections.defaultdict(set)   # stop: buses going through that stop
        
        for bus_number, route in enumerate(routes):
            for stop in route:
                graph[stop].add(bus_number)
        
        queue.append((source, 0))   # (stop, no. of buses required to reach the stop)
        
        while queue:
            stop, num_of_buses = queue.popleft()
            
            if stop == target:
                return num_of_buses
            
            # find all the buses that pass 'stop' stop
            for bus_number in graph[stop]:
                # don't travel the same bus again
                # mark this bus as traveled
                if bus_number not in visited_buses:
                    visited_buses.add(bus_number)
                
                    # travel to all stops this bus goes to
                    for stop in routes[bus_number]:
                        if stop not in visited_stops:
                            queue.append((stop, num_of_buses + 1))
                            visited_stops.add(stop)
            
        return -1
    