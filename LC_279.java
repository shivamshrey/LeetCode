// 279. Perfect Squares

// TC: O(n√n)
// SC: O(n)
class Solution {
    public int numSquares(int n) {
        if (n <= 3)
            return n; 
        int[] dp = new int[n + 1];
        
        for (int i = 0; i <= n; i++) {
            // any number n can be formed by adding 1^2 n times
            // which is the maximum squares required in the worst case
            dp[i] = i;
            // check for all possible perfect sum breakpoints
            for (int j = 1; j * j <= i; j++) {
                dp[i] = Math.min(dp[i], dp[i - j * j] + 1);    
            }
        }
        
        return dp[n];
    }
}
