class Solution {
    public int oddCells(int n, int m, int[][] indices) {
        int count = 0;
        int[] rowInc = new int[n];
        int[] colInc = new int[m];
        
        for (int[] index : indices) {
            rowInc[index[0]]++;
            colInc[index[1]]++;
        }
        
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                if ((rowInc[i] + colInc[j]) % 2 != 0)
                    count++;
        
        return count;
    }
}
