// 62. Unique Paths

class Solution {;
    public int uniquePaths(int m, int n) {
        int R = Math.min(m, n) - 1;
        
        // Calculate combination nCr value
        double nCr = 1;
        for (int i = 1; i <= R; i++) {
            nCr = nCr * (m + n - i - 1) / i;
        }
        
        return (int) nCr;
    }
}
