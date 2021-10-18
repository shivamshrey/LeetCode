// 1094. Car Pooling

// TC: O(n), n = no. of trips
// SC: O(m), m = no. of stops

class Solution {
    public boolean carPooling(int[][] trips, int capacity) {
        int[] stops = new int[1001];
        for (int[] trip : trips) {
            stops[trip[1]] += trip[0];
            stops[trip[2]] -= trip[0];
        }
        
        int i = 0;
        while (i < stops.length && capacity >= 0)
            capacity -= stops[i++];
        
        return capacity >= 0;
    }
}
