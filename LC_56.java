// 56. Merge Intervals

class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1)
            return intervals;
        Arrays.sort(intervals, (arr1, arr2) -> Integer.compare(arr1[0], arr2[0]));
        
        List<int[]> result = new ArrayList<>();
        result.add(intervals[0]);
        
        for (int i = 0; i < intervals.length; i++) {
            if (result.get(result.size() - 1)[1] >= intervals[i][0])
                result.get(result.size() - 1)[1] = Math.max(intervals[i][1], result.get(result.size() - 1)[1]);
            else
                result.add(intervals[i]);
            
        }
        
        return result.toArray(new int[result.size()][]);
    }
}
