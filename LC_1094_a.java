// 1094. Car Pooling

// TC: O(n log n), n = no. of trips
// SC: O(n)

class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        // Map to store no. of passengers in the car at every stop in sorted order of stops
        Map<Integer, Integer> stops = new TreeMap<>();
        for (int[] trip : trips) {
            stops.put(trip[1], stops.getOrDefault(trip[1], 0) + trip[0]);
            stops.put(trip[2], stops.getOrDefault(trip[2], 0) - trip[0]);
        }
        
        for (int passengers : stops.values()) {
            capacity -= passengers;
            if (capacity < 0)
                return false;
        }
        
        return true;
    }
}
