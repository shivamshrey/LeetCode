// 416. Partition Equal Subset Sum

class Solution {
    public boolean canPartition(int[] nums) {
        int sum = IntStream.of(nums).sum();
        if (sum % 2 != 0)
            return false;
        
        int n = nums.length;
        sum /= 2;
        boolean[] dp = new boolean[sum + 1];
        dp[0] = true;
        for (int num : nums) {
            for (int j = sum; j >= num; j--) {
                if (dp[j - num] || j == num) dp[j] = true;
            }
        }
        
        return dp[sum];
    }
}
