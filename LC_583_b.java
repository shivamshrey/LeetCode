// 583. Delete Operation for Two Strings

class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        
        int[][] lcs = new int[m + 1][n + 1];
        
        for (int i = 0; i <= m; i++)
            lcs[i][0] = 0;
        
        for (int j = 0; j <= n; j++)
            lcs[0][j] = 0;
        
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0 || j == 0) {
                    lcs[i][j] = i + j;
                } else if (word1.charAt(i - 1) == word2.charAt(j - 1))
                    lcs[i][j] = lcs[i - 1][j - 1];
                else
                    lcs[i][j] = 1 + Math.min(lcs[i - 1][j], lcs[i][j - 1]);
            }
        }
        
        return lcs[m][n];
    }
}
