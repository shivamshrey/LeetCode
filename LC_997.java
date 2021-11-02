// 997. Find the Town Judge

class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] degrees = new int[n + 1];
        
        for (int[] t : trust) {
            degrees[t[0]]--;
            degrees[t[1]]++;
        }
        
        for (int i = 1; i <= n; i++) {
            if (degrees[i] == n - 1)
                return i;
        }
        
        return -1;
    }
}
