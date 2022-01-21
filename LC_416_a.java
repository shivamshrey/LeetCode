// 416. Partition Equal Subset Sum

class Solution {
    public boolean canPartition(int[] nums) {
        int sum = IntStream.of(nums).sum();
        if (sum % 2 != 0)
            return false;
        int n = nums.length;
        sum /= 2;
        boolean[][] dp = new boolean[n + 1][sum + 1];
        for(int i = 0; i <= n; i++) dp[i][0] = true; //subset with 0 sum
        
        for(int j = 1; j <= sum; j++) dp[0][j] = false; //non-zero sum with 0 elements
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= sum; j++) {
                // exclude ith element if its > than remainder sum
                if (nums[i - 1] > j)
                    dp[i][j] = dp[i - 1][j];
                else
                    dp[i][j] = dp[i - 1][j] || dp[i - 1][j - nums[i - 1]];
            }
        }            
        
        return dp[n][sum];
    }
}
