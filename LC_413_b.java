// 413. Arithmetic Slices

class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int dp = 0, result = 0;
        
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]) {
                dp = dp + 1;
                result += dp;
            } else {
                dp = 0;
            }
        }
        
        return result;
    }
}
