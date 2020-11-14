// 57. Insert Interval

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        int newStart = newInterval[0];
        int newEnd = newInterval[1];
        List<int[]> result = new ArrayList<>();
        
        for (int[] interval : intervals) {
            int curStart = interval[0];
            int curEnd = interval[1];
            if (curEnd < newStart)
                result.add(interval);
            else if (newEnd < curStart) {
                result.add(new int[] {newStart, newEnd});
                newStart = curStart;
                newEnd = curEnd;
            } else {
                newStart = Math.min(curStart, newStart);
                newEnd = Math.max(curEnd, newEnd);
            }
        }
        result.add(new int[] {newStart, newEnd});
        
        return result.toArray(new int[result.size()][2]);
    }
}
