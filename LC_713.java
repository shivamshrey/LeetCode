// 713. Subarray Product Less Than K

class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k <= 1) return 0;
        
        int product = 1, start = 0, result = 0;
        for (int end = 0; end < nums.length; end++) {
            product *= nums[end];
            while (product >= k)
                product /= nums[start++];
            result += end - start + 1;
        }
        return result;
    }
}
