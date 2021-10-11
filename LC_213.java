// 213. House Robber II

class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1)
            return nums[0];
        return Math.max(robUtil(nums, 0, nums.length - 2),
                        robUtil(nums, 1, nums.length - 1));
    }
    
    public int robUtil(int[] nums, int start, int end) {
        int prev = 0, cur = 0, newRob = 0;
        for (int i = start; i <= end; i++) {
            newRob = Math.max(nums[i] + prev, cur);
            prev = cur;
            cur = newRob;
        }
        
        return newRob;
    }
}
