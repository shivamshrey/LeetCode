// 221. Maximal Square

class Solution {
    public int maximalSquare(char[][] matrix) {
        // dp[i][j] = side length of max square that can be formed whose bottom right corner is (i - 1, j - 1) in the original matrix
        int[][] dp = new int[matrix.length + 1][matrix[0].length + 1];
        int maxLen = 0;
        for (int i = 1; i <= matrix.length; i++) {
            for (int j = 1; j <= matrix[0].length; j++) {
                if (matrix[i - 1][j - 1] == '1') {
                    dp[i][j] = Math.min(dp[i - 1][j - 1], 
                                        Math.min(dp[i - 1][j], dp[i][j - 1]))
                                            + 1;
                    maxLen = Math.max(maxLen, dp[i][j]);
                }
            }
        }
        return maxLen * maxLen;
    }
}