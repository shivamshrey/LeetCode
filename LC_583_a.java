// 583. Delete Operation for Two Strings

class Solution {
    public int minDistance(String word1, String word2) {
        return word1.length() + word2.length() - 2 * longestCommonSubsequence(word1, word2);
    }
    
    private int longestCommonSubsequence(String word1, String word2) {
        int m = word1.length();
        int n = word2.length();
        
        int[][] lcs = new int[m + 1][n + 1];
        
        for (int i = 0; i <= m; i++)
            lcs[i][0] = 0;
        
        for (int j = 0; j <= n; j++)
            lcs[0][j] = 0;
        
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1))
                    lcs[i][j] = lcs[i - 1][j - 1] + 1;
                else
                    lcs[i][j] = Math.max(lcs[i - 1][j], lcs[i][j - 1]);
            }
        }
        
        return lcs[m][n];
    }
}
