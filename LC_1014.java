// 1014. Best Sightseeing Pair

class Solution {
    public int maxScoreSightseeingPair(int[] values) {
        int result = Integer.MIN_VALUE;
        int valuePlusIndex = values[0] + 0;
        
        for (int j = 1; j < values.length; j++) {
            result = Math.max(result, valuePlusIndex + values[j] - j);
            valuePlusIndex = Math.max(valuePlusIndex, values[j] + j);
        }
        return result;
    }
}
