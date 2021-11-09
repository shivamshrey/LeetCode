// 986. Interval List Intersections

class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        List<int[]> result = new ArrayList<>();
        int i = 0, j = 0;
        while (i < firstList.length && j < secondList.length) {
            // check if  firstList[i] intersects secondList[j]
            // start - start of intersection
            // end - end of intersection
            int start = Math.max(firstList[i][0], secondList[j][0]);
            int end = Math.min(firstList[i][1], secondList[j][1]);
            if (start <= end)   // true only in case of intersection
                result.add(new int[] {start, end});
            
            // increment pointer of the list with lower end value of interval
            if (firstList[i][1] < secondList[j][1])
                i++;
            else
                j++;
        }
        
        return result.toArray(new int[result.size()][]);
    }
}
